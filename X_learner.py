import pandas as pd
import numpy as np
from methods import get_prop_score, X_learner

DATA_PATH = 'data_frames/df_prep.csv'

if __name__ == '__main__':

    # load data
    df = pd.read_csv(DATA_PATH, encoding="ISO-8859-1")

    treatments = ['liveness_binary', 'danceability_binary']

    for treatment in treatments:

        print('Treatment "{}" results'.format(treatment))

        covariates_arr = df.drop([treatment, 'time_signature', 'popularity', 'track_id'], axis=1).values
        treatment_arr = df[[treatment]].values.reshape(-1)
        time_signature_arr = df[['time_signature']].values.reshape(-1)
        outcome_arr = df[['popularity']].values.reshape(-1)

        # calculate propensity scores
        prop_scores_arr = get_prop_score(covariates_arr, treatment_arr)

        time_signature = [1, 3, 4, 5]
        print('-------------------------------')

        for ts in time_signature:

            ts_ind = np.where(time_signature_arr == ts)[0]
            p_cov = covariates_arr[ts_ind]
            p_treat = treatment_arr[ts_ind]
            p_outcome = outcome_arr[ts_ind]
            p_prop_scores = prop_scores_arr[ts_ind]

            # separate treated and control
            treated_ind = np.where(p_treat == 1)[0]
            control_ind = np.where(p_treat == 0)[0]

            x_learner_cate = X_learner(p_cov, p_outcome, treated_ind, control_ind, p_prop_scores)
            print('For time-signature %.0f,' %ts,' the CATE using X-Learner is %.4f'  %x_learner_cate)
