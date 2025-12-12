# Campus Mood Mapper - Deployment URLs

## Deployed Instances

### Render.com (Free Tier)
**Status**: ✅ Successfully Deployed
**URL**: https://campus-mood-mapper.onrender.com
**Service ID**: srv-d4u3ovmr433s73d9rkc0
**Instance Type**: Free (512 MB RAM, 0.1 CPU)
**Features**:
- Automatic scaling
- Docker-based deployment
- GitHub integration
- Free tier with inactivity spin-down

**API Endpoints**:
- Health Check: https://campus-mood-mapper.onrender.com/health
- FastAPI Docs: https://campus-mood-mapper.onrender.com/docs
- ReDoc: https://campus-mood-mapper.onrender.com/redoc

**Deployment Notes**:
- Free tier instances spin down after 15 minutes of inactivity
- Initial request will take 30-50 seconds as the instance wakes up
- No cold start costs - completely free
- Suitable for development and testing

### Railway.app (Pending)
**Status**: 🔄 In Progress
**Notes**: Repository loading was in progress during deployment setup

## Quick Start

### Testing the Render Deployment

```bash
# Test health endpoint
curl https://campus-mood-mapper.onrender.com/health

# Access FastAPI documentation
https://campus-mood-mapper.onrender.com/docs

# Access mood analysis endpoint (example)
curl -X POST https://campus-mood-mapper.onrender.com/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I am feeling great today!"}'
```

## Deployment Configuration

### Render.com Configuration
- **Branch**: main
- **Region**: Oregon (US West)
- **Runtime**: Docker
- **Start Command**: Automatically detected from Dockerfile
- **Environment Variables**: None required (can be added via dashboard)

## Future Deployments

Additional free platforms that can be configured:
- Railway.app (₹100 free credit/month)
- PythonAnywhere.com (free tier)
- Heroku (via hobby tier upgrade)
- AWS Free Tier
- Google Cloud Free Tier

## Monitoring & Logs

View deployment logs in Render dashboard:
https://dashboard.render.com/web/srv-d4u3ovmr433s73d9rkc0/logs

## Support & Documentation

- [Render Documentation](https://render.com/docs)
- [Docker Documentation](https://docs.docker.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Project DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
