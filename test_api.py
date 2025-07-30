#!/usr/bin/env python3
"""
Test script for the Crop Yield Prediction API
Run this to test your API before deploying to Vercel
"""

import requests
import json

# Test configuration
BASE_URL = "http://localhost:5000"  # Change this to your Vercel URL when testing deployed version

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_database_connection():
    """Test database connection endpoint"""
    print("\n🔍 Testing database connection...")
    try:
        response = requests.get(f"{BASE_URL}/check-db")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_prediction():
    """Test prediction endpoint"""
    print("\n🔍 Testing prediction...")
    try:
        test_data = {
            "Year": 2023,
            "average_rain_fall_mm_per_year": 1200,
            "pesticides_tonnes": 50,
            "avg_temp": 25.5,
            "Area": "India",
            "Item": "Rice",
            "user_id": "test_user"
        }
        
        response = requests.post(
            f"{BASE_URL}/predict",
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_user_registration():
    """Test user registration"""
    print("\n🔍 Testing user registration...")
    try:
        test_user = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        
        response = requests.post(
            f"{BASE_URL}/register",
            json=test_user,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting API Tests...")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health_check),
        ("Database Connection", test_database_connection),
        ("User Registration", test_user_registration),
        ("Prediction", test_prediction),
    ]
    
    results = {}
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    print(f"\n🎯 Overall: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    if all_passed:
        print("\n🚀 Your API is ready for deployment!")
    else:
        print("\n🔧 Please fix the failing tests before deploying.")

if __name__ == "__main__":
    main()
