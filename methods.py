import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split

def get_prop_score(covariates, treatment):
    '''
    calculate propensity score function based on logistic regression
    :param covariates: data covariates
    :param treatment: data treatments
    :return: propensity score function
    '''

    # separate data to train and test
    x_train, x_test, y_train, y_test = train_test_split(covariates, treatment, test_size=0.15, random_state=42)

    # train & test logistic regression model
    prop_score_func = LogisticRegression(penalty='l2', random_state=1200).fit(X=x_train, y=y_train)
    #print('logistic regression classification accuracy is:', prop_score_func.score(x_test, y_test))

    propensity_scores = np.empty(covariates.shape[0])
    for i in range(covariates.shape[0]):
        propensity_scores[i] = prop_score_func.predict_proba(covariates[i].reshape(1, -1))[0][1] # P(t=1|x)

    return propensity_scores

def X_learner(covariates, outcome, treated_ind, control_ind, prop_scores):
    '''
    calculate average treatment effect based on X-learner method
    :param covariates: data covariates
    :param outcome: data outcome
    :param treated_ind: indexes of the treated samples
    :param control_ind: indexes of the control samples
    :return: average treatment effect
    '''

    treated_covariates = covariates[treated_ind]
    control_covariates = covariates[control_ind]

    treated_model = LinearRegression().fit(X=treated_covariates, y=outcome[treated_ind])
    control_model = LinearRegression().fit(X=control_covariates, y=outcome[control_ind])

    x_learner_treated = LinearRegression().\
        fit(X=treated_covariates, y=outcome[treated_ind] - control_model.predict(treated_covariates))
    x_learner_control = LinearRegression(). \
        fit(X=control_covariates, y=outcome[control_ind] - treated_model.predict(control_covariates))

    te_sum = 0
    for i in range(covariates.shape[0]):
        te_sum += (1 - prop_scores[i]) * (x_learner_treated.predict(covariates[i].reshape(1, -1))[0]) \
                         - prop_scores[i] * (x_learner_control.predict(covariates[i].reshape(1, -1))[0])

    return te_sum / covariates.shape[0]