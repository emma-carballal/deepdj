
from deepdj_processing import deepdj_processing

if __name__ == '__main__':

    dj = deepdj_processing('data/tcc_ceds_music_cleaned.csv')
    res = dj.prompt_process()
    print(res)
    res = dj.prompt_process()
    print(res)
