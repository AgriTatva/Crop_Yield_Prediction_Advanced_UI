# Vercel Deployment Guide

This guide will help you deploy your Crop Yield Prediction application to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **MongoDB Atlas**: Set up a MongoDB Atlas cluster
3. **GitHub Repository**: Push your code to GitHub

## Deployment Steps

### 1. Install Vercel CLI

```bash
npm i -g vercel
```

### 2. Login to Vercel

```bash
vercel login
```

### 3. Deploy from Project Root

```bash
vercel
```

### 4. Configure Environment Variables

In your Vercel dashboard:

1. Go to your project → Settings → Environment Variables
2. Add these variables:

```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/crop_yield_db
MONGODB_DB_NAME=crop_yield_db
FRONTEND_URL=https://your-frontend-domain.vercel.app
```

### 5. Project Structure for Vercel

```
├── api/                    # Backend serverless functions
│   ├── app.py             # Main Flask application
│   ├── dtr.pkl            # Decision Tree model
│   ├── preprocessor.pkl   # Data preprocessor
│   └── requirements.txt   # Python dependencies
├── vercel.json            # Vercel configuration
└── ... (other frontend files)
```

## Important Notes

### Backend API Endpoints

Once deployed, your API will be available at:
- `https://your-project.vercel.app/predict`
- `https://your-project.vercel.app/register`
- `https://your-project.vercel.app/login`
- `https://your-project.vercel.app/history`
- etc.

### Frontend Configuration

Update your React frontend to use the production API URL:

```javascript
const API_URL = process.env.NODE_ENV === 'production' 
  ? 'https://your-project.vercel.app' 
  : 'http://localhost:5000';
```

### Serverless Limitations

- **Timeout**: 10 seconds for Hobby plan, 60 seconds for Pro
- **Memory**: 1024MB for Hobby plan
- **Cold Starts**: Models reload on each cold start

### Troubleshooting

1. **Model Loading Issues**: Ensure pkl files are in the `api/` directory
2. **Database Connection**: Verify MongoDB URI in environment variables
3. **CORS Issues**: Check CORS configuration in `api/app.py`
4. **Dependencies**: Verify all packages are in `api/requirements.txt`

## Local Development

To test the API structure locally:

```bash
cd api
python app.py
```

The API will be available at `http://localhost:5000`

## Deployment Commands

```bash
# Deploy to production
vercel --prod

# Deploy preview (staging)
vercel

# Check deployment status
vercel ls

# View logs
vercel logs [deployment-url]
```
