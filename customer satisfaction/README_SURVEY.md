# Customer Satisfaction Survey System 🎯

An animated, responsive web-based customer satisfaction survey system that predicts customer satisfaction levels based on flight service ratings.

## 🌟 Features

### Frontend (Web Form)
- **Animated Interface**: Smooth animations and transitions for engaging user experience
- **Star Rating System**: Interactive 5-star rating for each service category
- **Progress Bar**: Visual feedback showing form completion progress
- **Responsive Design**: Mobile-friendly layout that works on all devices
- **Real-time Validation**: Instant feedback on user inputs
- **Loading Animations**: Professional loading states during prediction

### Backend (Flask API)
- **Enhanced Prediction Algorithm**: Improved satisfaction prediction based on rating patterns
- **Comprehensive Error Handling**: Robust error management and user-friendly messages
- **Logging System**: Detailed logging for monitoring and debugging
- **Health Check**: API endpoint for system monitoring
- **CORS Support**: Ready for cross-origin requests

### Data Integration
- **Filtered Dataset**: Uses cleaned customer satisfaction data (`cust_satisfaction_model_cleaned.csv`)
- **Three Key Metrics**: 
  - Inflight Entertainment (1-5 stars)
  - Baggage Handling (1-5 stars) 
  - Cleanliness (1-5 stars)

## 🚀 Quick Start

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt
```

### Option 1: Quick Launch
```bash
# Run the startup script
python start_survey.py
```

### Option 2: Manual Launch
```bash
# Start the Flask application
python "main (1).py"
```

### Access the Survey
Open your browser and navigate to: `http://localhost:5000`

## 📋 Survey Flow

1. **Welcome Screen**: Users see an animated welcome message
2. **Rating Process**: Users rate three service categories using interactive stars
3. **Progress Tracking**: Visual progress bar shows completion status
4. **Prediction**: System calculates satisfaction prediction based on ratings
5. **Results**: Animated results display with confidence levels

## 🔧 Technical Details

### Prediction Logic
```python
# Rating scale interpretation
4.5+ stars → "Highly Satisfied" (92% confidence)
4.0+ stars → "Satisfied" (85% confidence)
3.0+ stars → "Neutral/Moderate" (75% confidence)
2.0+ stars → "Dissatisfied" (82% confidence)
<2.0 stars → "Highly Dissatisfied" (88% confidence)
```

### API Endpoints
- `GET /` - Serve the main survey page
- `POST /predict` - Submit ratings and get prediction
- `GET /api/health` - System health check
- `GET /api/survey-stats` - Basic survey statistics

### File Structure
```
cust satisfaction/
├── templates/
│   └── index.html          # Animated survey form
├── start_survey.py         # Startup script
├── main (1).py             # Flask application
├── requirements.txt        # Python dependencies
├── cust_satisfaction_model_cleaned.csv  # Filtered dataset
└── README_SURVEY.md        # This documentation
```

## 🎨 Customization

### Changing Colors
Edit the CSS variables in `templates/index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Modifying Rating Categories
Update both frontend and backend:
1. Add new form fields in `templates/index.html`
2. Update validation in `main (1).py`
3. Adjust prediction logic accordingly

### Enhancing Animations
The system uses CSS animations:
- `@keyframes slideIn` - Container entrance
- `@keyframes fadeIn` - Form field animations
- `@keyframes pulse` - Button animations
- `@keyframes float` - Icon floating effects

## 📊 Data Integration

The system is designed to work with your filtered dataset:
- **Input**: User ratings (1-5 stars) for three service categories
- **Processing**: Average rating calculation and satisfaction prediction
- **Output**: Satisfaction level with confidence score

### Sample API Response
```json
{
    "prediction": "satisfied",
    "confidence": 0.85,
    "status": "success",
    "avg_rating": 4.33,
    "message": "Good ratings indicate satisfied customer.",
    "individual_ratings": {
        "entertainment": 4,
        "baggage": 5,
        "cleanliness": 4
    },
    "timestamp": "2024-03-14 10:30:45"
}
```

## 🔒 Security Features

- Input validation and sanitization
- Rate limiting ready (can be added)
- Error messages don't expose system details
- CORS configuration for production deployment

## 🐛 Error Handling

The system handles various error scenarios:
- Missing or invalid ratings
- Network connectivity issues
- Server-side processing errors
- Invalid data formats

## 📱 Mobile Optimization

- Responsive grid layout
- Touch-friendly star ratings
- Optimized for small screens
- Fast loading on mobile networks

## 🚀 Deployment

### Development
```bash
python start_survey.py
```

### Production
Consider using:
- Gunicorn WSGI server
- Nginx reverse proxy
- Environment variables for configuration
- Database for storing survey results

## 📈 Future Enhancements

- Database integration for result storage
- Advanced analytics dashboard
- Email notifications for low satisfaction
- Multi-language support
- Additional service categories
- Machine learning model integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Check the error logs in the console
- Verify all dependencies are installed
- Ensure the Flask app is running on port 5000
- Check browser developer tools for frontend issues

---

**Happy surveying! 🎉**