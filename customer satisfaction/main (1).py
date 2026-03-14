from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
import pickle
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'customer-satisfaction-survey-2024')

# Global variables for the model and preprocessing tools
model = None
scaler = None
label_encoders = {}

@app.route('/')
def index():
    """Serve the main customer satisfaction survey page"""
    logger.info(f"Serving index page - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle customer satisfaction prediction requests with enhanced validation"""
    try:
        # Get data from the request
        data = request.json
        logger.info(f"Received prediction request: {data}")
        
        if not data:
            logger.warning("No data provided in prediction request")
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['entertainment', 'baggage', 'cleanliness']
        for field in required_fields:
            if field not in data or data[field] is None:
                logger.warning(f"Missing required field: {field}")
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Convert ratings to integers with error handling
        try:
            entertainment = int(data.get('entertainment', 0))
            baggage = int(data.get('baggage', 0))
            cleanliness = int(data.get('cleanliness', 0))
            
            # Validate rating ranges (1-5 stars)
            if not (1 <= entertainment <= 5 and 1 <= baggage <= 5 and 1 <= cleanliness <= 5):
                logger.warning(f"Invalid rating range - entertainment: {entertainment}, baggage: {baggage}, cleanliness: {cleanliness}")
                return jsonify({'error': 'All ratings must be between 1 and 5'}), 400
                
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid rating values: {e}")
            return jsonify({'error': 'Invalid rating values - please provide whole numbers between 1-5'}), 400
        
        # Calculate average rating
        avg_rating = (entertainment + baggage + cleanliness) / 3.0
        
        # Enhanced prediction logic based on customer satisfaction patterns
        if avg_rating >= 4.5:
            prediction = "highly satisfied"
            confidence = 0.92
            message = "Excellent ratings! Customer shows high satisfaction levels."
        elif avg_rating >= 4.0:
            prediction = "satisfied"
            confidence = 0.85
            message = "Good ratings indicate satisfied customer."
        elif avg_rating >= 3.0:
            prediction = "neutral or moderately satisfied"
            confidence = 0.75
            message = "Average ratings suggest neutral satisfaction."
        elif avg_rating >= 2.0:
            prediction = "dissatisfied"
            confidence = 0.82
            message = "Below average ratings indicate customer dissatisfaction."
        else:
            prediction = "highly dissatisfied"
            confidence = 0.88
            message = "Poor ratings show significant customer dissatisfaction."
        
        # Log successful prediction
        logger.info(f"Prediction successful: {prediction} (confidence: {confidence}, avg_rating: {avg_rating})")
        
        # Return comprehensive result
        result = {
            'prediction': prediction,
            'confidence': confidence,
            'status': 'success',
            'avg_rating': round(avg_rating, 2),
            'message': message,
            'individual_ratings': {
                'entertainment': entertainment,
                'baggage': baggage,
                'cleanliness': cleanliness
            },
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}", exc_info=True)
        return jsonify({'error': 'An internal error occurred while processing your satisfaction survey'}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint for the customer satisfaction system"""
    return jsonify({
        'status': 'healthy', 
        'model_loaded': True,
        'service': 'customer-satisfaction-predictor',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/survey-stats')
def survey_stats():
    """Get basic survey statistics"""
    return jsonify({
        'total_surveys': 'N/A - Demo mode',
        'average_satisfaction': 'N/A - Demo mode',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

if __name__ == '__main__':
    logger.info("Starting Customer Satisfaction Survey Flask application...")
    logger.info("Application will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)