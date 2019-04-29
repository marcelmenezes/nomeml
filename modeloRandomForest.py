from formatoModelo import getDataFrameModelo
from sklearn.externals import joblib
est_RandomForest = joblib.load('modelo_RandomForest.pkl')
est_SVC = joblib.load('modelo_SVC.pkl')

def getSexo(nome:str):
    df = getDataFrameModelo(nome)
    #return 'M' if reg.predict(df)[0] == 1 else 'F'
    est = est_RandomForest
    proba = est.predict_proba(df)
    prob = {'F': proba[0][0], 'M': proba[0][1]}
    return 'M' if est.predict(df)[0] == 1 else 'F', prob

    #return 'M'
    # print("predict: ", nome)
    # print("predict: ", reg.predict(df))
    # print("proba: ", reg.predict_proba(df))



def getSexo(nome:str):
    df = getDataFrameModelo(nome)
    #return 'M' if reg.predict(df)[0] == 1 else 'F'
    est = est_SVC
    return 'M' if est.predict(df)[0] == 1 else 'F'

    #return 'M'
    # print("predict: ", nome)
    # print("predict: ", reg.predict(df))
    # print("proba: ", reg.predict_proba(df))
