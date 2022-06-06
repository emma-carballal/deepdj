
# ----------------------------------
#         LOCAL SET UP
# ----------------------------------

install_requirements:
	@pip install -r requirements.txt

# ----------------------------------
#         HEROKU COMMANDS
# ----------------------------------

streamlit:
	-@streamlit run app.py

heroku_login:
	-@heroku login

heroku_create_app:
	-@heroku create ${APP_NAME}

deploy_heroku:
	-@git push heroku master
	-@heroku ps:scale web=1

# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------
install:
	@pip install . -U

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info
	-@rm model.joblib

run_api:
	uvicorn api.fast:app --reload

build_image:
	docker build --tag=deepdj .

push_gcp:
	export PROJECT_ID=deepdj
	gcloud config set project $$PROJECT_ID
	export DOCKER_IMAGE_NAME=deepdj
	docker build -t eu.gcr.io/$$PROJECT_ID/$$DOCKER_IMAGE_NAME .
	docker push eu.gcr.io/$$PROJECT_ID/$$DOCKER_IMAGE_NAME

deploy_gcp:
	gcloud run deploy --image eu.gcr.io/$$PROJECT_ID/$$DOCKER_IMAGE_NAME --platform managed --region europe-west1 --set-env-vars "GOOGLE_APPLICATION_CREDENTIALS=/lunar-inn-346918-f23c3084971a.json"
