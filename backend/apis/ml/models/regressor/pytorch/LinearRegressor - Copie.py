import sys, os, pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split


# importing ml folder
ml_folder = os.path.dirname(os.path.abspath('../'))
sys.path.insert(0,ml_folder)
from core.unavailable_columns import unavailable_columns
from core.get_label_type import get_label_type


class LinearRegressorModel:
    def __init__(self):
        # Instantiating a LinearRegressor Model
        self.model = LinearRegression()
        self.model_name = "LinearRegressor"

    def read_data(self, url:str, sep:str=","):
        df = pd.read_csv(url, sep=sep)
        return df

    def split_data(self, features, label, shuffle:bool=True, train_size:float=0.3, random_state=42):
        return train_test_split(features, label, shuffle=shuffle, train_size=train_size, random_state=random_state)
    
    def train_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe
        self.model.fit(X_train, y_train)

    def predict_data(self, dataframe):
        X_train, X_test, y_train, y_test = dataframe

        # self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        return predictions

    def evaluate_data(self, y_test, predictions):
        r2   = r2_score(y_test, predictions)
        rmse = mean_squared_error(y_test, predictions)
        mae  = mean_absolute_error(y_test, predictions)

        output = [ str(i)+","+str(j) for i,j in zip(predictions, y_test) ]

        result = {"rmse":rmse, "mae":mae, "r2":r2, "output":output}
        
        return result


# =====================================================================================


#
# # LabelEncoder  ---> attribut des valeurs numeriques au variables categorielles
# # lbl_encoder = LabelEncoder()
# # df['pays_new'] = lbl_encoder.fit_transform(df['pays'])
# #  > cotonou = 37
# #  > bohicon = 88
# #  > allada  = 3
# # OnehotEncoder ---> creer de nouvel colonne portant le nom de la variable et define 1 si correct 0 sinon
# # dummies_col = pd.get_dummies(df['pays'])
# # df = df.join(dummies_col)
#
# from sklearn.datasets import make_classification
# from sklearn.linear_model import LogisticRegression, LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import make_pipeline, Pipeline
# from sklearn.preprocessing import StandardScaler, RobustScaler
# from sklearn.decomposition import PCA
#
# import pandas as pd
#
# import sys, os
#
# # importing grand-parent folder
# ml_folder = os.path.dirname(os.path.abspath('../'))
# sys.path.insert(0,ml_folder)
#
# from core.unavailable_columns import unavailable_columns
#
# # =====
# df = pd.read_csv(ml_folder+'/core/data.csv')
# print(df.shape)
#
#
#
#
#
# best_model:dict = {
#     "pipeline" : "",
#     "accuracy" : 0,
#     "classifier" : 0
# }
#
# #
# col_del = unavailable_columns(df)
# df.drop(col_del, axis=1, inplace=True)
#
# X_train = df['revenu']
# y_train = df['age']
#
# pipeline1 = Pipeline(steps=[
#     ('standardscaler', StandardScaler()),
#     ('robustscaler', RobustScaler()),
#     ('pca', PCA(n_components=1)),
#     ('linearegression', LinearRegression())
# ])
# pipeline2 = Pipeline(steps=[
#     ('standardscaler', StandardScaler()),
#     ('pca', PCA(n_components=1)),
#     ('logisticregression', LogisticRegression(solver='lbfgs', max_iter=1000))
# ])
#
# pipelines = [pipeline1, pipeline2]
# mdl = {0:'linear',1:'logistic'}
#
# for idx, i in enumerate(pipelines):
#     print(mdl[idx])
#     i.fit(df[['revenu']], y_train)  # apply scaling on training data
# print('---------')
#
# for idx, model in enumerate(pipelines):
#     if model.score(df[['revenu']], y_train) > best_model["accuracy"]:
#         best_model["pipeline"] = model
#         best_model["accuracy"] = model.score(df[['revenu']], y_train)
#         best_model["classifier"] = idx
#     print(mdl[idx],' <--> ', str(model.score(df[['revenu']], y_train)))  # apply scaling on training data
#
#
# print('---------')
# print('best_model: ', best_model)
# print('---------')
#
# for idx, i in enumerate(pipelines):
#     print(mdl[idx],i.predict([[209]]))







