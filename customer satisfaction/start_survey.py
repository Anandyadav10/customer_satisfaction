#!/usr/bin/env python3
"""
Customer Satisfaction Survey System Startup Script
Launches the Flask web application with enhanced logging and error handling
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
    try:
        import flask
        import pandas
        import numpy
        import sklearn
        print("✅ All required dependencies are available")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def setup_environment():
    """Setup environment variables and paths"""
    # Add current directory to Python path
    current_dir = Path(__file__).parent.absolute()
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    
    # Set environment variables
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    
    print(f"✅ Environment configured - Working directory: {current_dir}")

def launch_application():
    """Launch the Flask application"""
    try:
        print("🚀 Starting Customer Satisfaction Survey System...")
        print("📋 Features:")
        print("   • Animated web form with star ratings")
        print("   • Real-time satisfaction predictions")
        print("   • Responsive design for mobile devices")
        print("   • Enhanced error handling and logging")
        print()
        
        # Import and run the Flask app
        from main__ import app
        
        print("✅ Flask application loaded successfully")
        print("🌐 Opening browser at http://localhost:5000")
        print("⏹️  Press Ctrl+C to stop the server")
        print()
        
        # Open browser after a short delay
        time.sleep(2)
        webbrowser.open('http://localhost:5000')
        
        # Run the Flask application
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=False  # Disable reloader to prevent double startup
        )
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Customer Satisfaction Survey System stopped by user")
    except Exception as e:
        print(f"\n❌ Error launching application: {e}")
        sys.exit(1)

def main():
    """Main startup function"""
    print("🎯 Customer Satisfaction Survey System")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Setup environment
    setup_environment()
    
    # Launch application
    launch_application()

if __name__ == '__main__':
    main()