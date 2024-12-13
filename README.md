# udemy-ML-Deploy
Udemy-Udemy Machine Learning Model Deployment with Streamlit

## Deployment Notes

### Set Environment Variable
PYTHON_VERSION = 3.11.9

### Secrets Management in Render

Streamlit installs secrets in .streamlit/secrets.toml
Render store secrets in /etc/secrets/<name_of_secrets_file>

To fix, create the directory streamlit and copy the 
secrets.toml file inside during the build.

Render build command should be:
mkdir .streamlit; cp /etc/secrets/secrets.toml ./.streamlit/; 
    pip install --upgrade pip && pip install -r requirements.txt

