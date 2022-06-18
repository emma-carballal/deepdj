# DeepDJ: a bootcamp team project

DeepDJ is a music playlist creator based on a text promt.
This web app was created during the two final project weeks at the Le Wagon bootcamp in Berlin (April-June 2022).

## Background
Most music apps create playlists that are based on the music that you already listen to. Recommendations tend to be tracks that you already know or that are very similar, and may lead to a very monotonous listening experience.

DeepDJ is an app that allows you to enter a text prompt of any length (a description, a thought, a wish, a story, a poem...) and provides the best matches based on song lyrics. This is achieved by preprocessing and vectoryzing a large dataset of song lyrics ([Music Dataset : 1950 to 2019](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019) from Kaggle) and calculating the cosine distance between the vectorized prompt and the dataset of songs.

## Setup
To run this app locally:

1. Create a deepdj directory and clone the repository
  ```
  git clone https://github.com/emma-carballal/deepdj.git
  ```
2. Set up a deepdj virtual environment
```
pyenv virtualenv deepdj
```
3. Go to the project directory and set it to use the deepdj virtual environment
```
cd deepdj
pyenv run deepdj
```
6. Install the projects requirements
```
make install_requirements
```
8. Run the api
```
make run_api
```
10. Run the Streamlit app locally
```
make streamlit
```
## Links
Web app deployed on Heroku: https://deepdj.herokuapp.com/

## The team:
* [Gabriela Pimenta dos Reis](https://github.com/GabiPimenta29) (data sourcing and cleaning)
* [Hatice Peucker](https://github.com/chichi-pixel) (Streamlit interface)
* [Julia Strahl](https://github.com/juju-github) (API)
* [Emma Carballal Haire](https://github.com/emma-carballal) (pitch) (deployment on Heroku and Google Cloud Platform)

## License
DeepDJ is released under the MIT License. See [LICENSE](LICENCE) file for details.
