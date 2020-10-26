{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow import keras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\n",
    "  \"C:/Users/pradeep.kumar/Desktop/NLP/HealthCostPred.csv\",\n",
    "  parse_dates=['Year_month'],\n",
    "  index_col=\"Year_month\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cost_mx_rx</th>\n",
       "      <th>employee_count</th>\n",
       "      <th>chronic</th>\n",
       "      <th>0-25_countdist_pat</th>\n",
       "      <th>25-50_countdist_pat</th>\n",
       "      <th>50-75_countdist_pat</th>\n",
       "      <th>patient_count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Year_month</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>295996.81</td>\n",
       "      <td>464</td>\n",
       "      <td>124</td>\n",
       "      <td>308</td>\n",
       "      <td>316</td>\n",
       "      <td>314</td>\n",
       "      <td>938</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>239754.34</td>\n",
       "      <td>464</td>\n",
       "      <td>169</td>\n",
       "      <td>308</td>\n",
       "      <td>316</td>\n",
       "      <td>314</td>\n",
       "      <td>938</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>281825.84</td>\n",
       "      <td>466</td>\n",
       "      <td>213</td>\n",
       "      <td>310</td>\n",
       "      <td>316</td>\n",
       "      <td>317</td>\n",
       "      <td>943</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>335724.20</td>\n",
       "      <td>468</td>\n",
       "      <td>239</td>\n",
       "      <td>311</td>\n",
       "      <td>318</td>\n",
       "      <td>319</td>\n",
       "      <td>948</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>362122.97</td>\n",
       "      <td>476</td>\n",
       "      <td>272</td>\n",
       "      <td>319</td>\n",
       "      <td>319</td>\n",
       "      <td>327</td>\n",
       "      <td>965</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            cost_mx_rx  employee_count  chronic  0-25_countdist_pat  \\\n",
       "Year_month                                                            \n",
       "2017-01-01   295996.81             464      124                 308   \n",
       "2017-02-01   239754.34             464      169                 308   \n",
       "2017-03-01   281825.84             466      213                 310   \n",
       "2017-04-01   335724.20             468      239                 311   \n",
       "2017-05-01   362122.97             476      272                 319   \n",
       "\n",
       "            25-50_countdist_pat  50-75_countdist_pat  patient_count  \n",
       "Year_month                                                           \n",
       "2017-01-01                  316                  314            938  \n",
       "2017-02-01                  316                  314            938  \n",
       "2017-03-01                  316                  317            943  \n",
       "2017-04-01                  318                  319            948  \n",
       "2017-05-01                  319                  327            965  "
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(36, 7)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11d04b41848>"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.lineplot(x=df.index,y='cost_mx_rx',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11d04ae2c08>"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Ploting quarterly trends\n",
    "df_by_quarter = df.resample('Q').sum()\n",
    "sns.lineplot(x=df_by_quarter.index,y='cost_mx_rx',data=df_by_quarter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "18\n",
      "18\n",
      "(18, 7) (18, 7)\n"
     ]
    }
   ],
   "source": [
    "train_size = int(len(df)*0.5)\n",
    "test_size = len(df) - train_size\n",
    "print(train_size)\n",
    "print(test_size)\n",
    "train,test = df.iloc[0:train_size],df.iloc[train_size:len(df)]\n",
    "print(train.shape,test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scaling Data for passing LSTM \n",
    "from sklearn.preprocessing import RobustScaler\n",
    "\n",
    "f_columns = [\"employee_count\", \"chronic\", \"0-25_countdist_pat\",\"25-50_countdist_pat\",\"50-75_countdist_pat\",\"patient_count\"]\n",
    "f_cost = [\"cost_mx_rx\"]\n",
    "\n",
    "f_transformer = RobustScaler()\n",
    "cost_transformer = RobustScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [],
   "source": [
    "f_transformer = f_transformer.fit(train[f_columns].to_numpy())\n",
    "cost_transformer = cost_transformer.fit(train[f_cost])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:494: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self.obj[item] = s\n",
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:205: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self._setitem_with_indexer(indexer, value)\n",
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py:2: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  \n",
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:494: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self.obj[item] = s\n",
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\pandas\\core\\indexing.py:205: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  self._setitem_with_indexer(indexer, value)\n",
      "C:\\Users\\pradeep.kumar\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py:5: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  \"\"\"\n"
     ]
    }
   ],
   "source": [
    "train.loc[:, f_columns] = f_transformer.transform(train[f_columns].to_numpy())\n",
    "train.loc[:, f_cost] = cost_transformer.transform(train[f_cost].to_numpy())\n",
    "\n",
    "test.loc[:, f_columns] = f_transformer.transform(test[f_columns].to_numpy())\n",
    "test.loc[:, f_cost] = cost_transformer.transform(test[f_cost])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create dataset for LSTM format\n",
    "import numpy as np\n",
    "def create_dataset(X,y,time_steps=1):\n",
    "    Xs,ys = [],[]\n",
    "    for i in range(len(X) - time_steps):\n",
    "        v = X.iloc[i:(i + time_steps)].to_numpy()\n",
    "        Xs.append(v)\n",
    "        ys.append(y.iloc[i + time_steps])\n",
    "    return np.array(Xs),np.array(ys)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [],
   "source": [
    "TIME_STEPS = 1\n",
    "X_train, y_train = create_dataset(train, train.cost_mx_rx, time_steps = TIME_STEPS)\n",
    "X_test, y_test = create_dataset(test, test.cost_mx_rx, time_steps = TIME_STEPS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(17, 1, 7) (17,)\n"
     ]
    }
   ],
   "source": [
    "#Sample,Time steps,Features\n",
    "print(X_train.shape,y_train.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(17, 1, 7) (17,)\n"
     ]
    }
   ],
   "source": [
    "print(X_test.shape,y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = keras.Sequential()\n",
    "model.add(\n",
    "  keras.layers.Bidirectional(\n",
    "    keras.layers.LSTM(\n",
    "      units=128,\n",
    "      input_shape=(X_train.shape[1], X_train.shape[2])\n",
    "    )\n",
    "  )\n",
    ")\n",
    "model.add(keras.layers.Dropout(rate=0.2))\n",
    "model.add(keras.layers.Dense(units=1))\n",
    "model.compile(loss='mean_squared_error', optimizer='adam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/40\n",
      "13/13 [==============================] - 1s 40ms/step - loss: 1.2212 - val_loss: 3.9897\n",
      "Epoch 2/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 1.1257 - val_loss: 3.8875\n",
      "Epoch 3/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 1.0755 - val_loss: 3.8266\n",
      "Epoch 4/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 1.0426 - val_loss: 3.7835\n",
      "Epoch 5/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 1.0281 - val_loss: 3.7663\n",
      "Epoch 6/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 1.0093 - val_loss: 3.7566\n",
      "Epoch 7/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.9973 - val_loss: 3.7552\n",
      "Epoch 8/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9896 - val_loss: 3.7640\n",
      "Epoch 9/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9498 - val_loss: 3.7741\n",
      "Epoch 10/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.9601 - val_loss: 3.7860\n",
      "Epoch 11/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9342 - val_loss: 3.7940\n",
      "Epoch 12/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9397 - val_loss: 3.7992\n",
      "Epoch 13/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9325 - val_loss: 3.8019\n",
      "Epoch 14/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.9073 - val_loss: 3.8028\n",
      "Epoch 15/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8941 - val_loss: 3.8080\n",
      "Epoch 16/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.9094 - val_loss: 3.8151\n",
      "Epoch 17/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8958 - val_loss: 3.8113\n",
      "Epoch 18/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8940 - val_loss: 3.8062\n",
      "Epoch 19/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8731 - val_loss: 3.8106\n",
      "Epoch 20/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8798 - val_loss: 3.7972\n",
      "Epoch 21/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8666 - val_loss: 3.7872\n",
      "Epoch 22/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8539 - val_loss: 3.7810\n",
      "Epoch 23/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8353 - val_loss: 3.7660\n",
      "Epoch 24/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8425 - val_loss: 3.7604\n",
      "Epoch 25/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8380 - val_loss: 3.7628\n",
      "Epoch 26/40\n",
      "13/13 [==============================] - 0s 2ms/step - loss: 0.8325 - val_loss: 3.7575\n",
      "Epoch 27/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8130 - val_loss: 3.7570\n",
      "Epoch 28/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.8011 - val_loss: 3.7464\n",
      "Epoch 29/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7778 - val_loss: 3.7356\n",
      "Epoch 30/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7813 - val_loss: 3.7254\n",
      "Epoch 31/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7637 - val_loss: 3.7191\n",
      "Epoch 32/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7640 - val_loss: 3.7209\n",
      "Epoch 33/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7740 - val_loss: 3.7269\n",
      "Epoch 34/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7559 - val_loss: 3.7274\n",
      "Epoch 35/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7470 - val_loss: 3.7262\n",
      "Epoch 36/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7526 - val_loss: 3.7271\n",
      "Epoch 37/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7175 - val_loss: 3.7326\n",
      "Epoch 38/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7157 - val_loss: 3.7328\n",
      "Epoch 39/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7075 - val_loss: 3.7400\n",
      "Epoch 40/40\n",
      "13/13 [==============================] - 0s 3ms/step - loss: 0.7137 - val_loss: 3.7548\n"
     ]
    }
   ],
   "source": [
    "history = model.fit(\n",
    "    X_train, y_train,\n",
    "    epochs=40,\n",
    "    batch_size=1,\n",
    "    validation_split=0.2,\n",
    "    shuffle=False\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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FC/M73HO/Xzk8uEB75x71My+a2aVzrmW7JUqIrPFeGfSp0thYeHg9JNPPskTTzzBc889R0FBAZdccsmoXQJjsdjgdDgcpre397TUmi2T6eViwA+A3c6528ZYZ76/HmZ2ob/d1mwWKiIynuLiYjo7O0dd1t7eTnl5OQUFBezZs4fnn3/+NFd3ekzmDH098CfAy2a2zX/tS8BiAOfcncAG4EYzSwG9wEbnnJuGekVERlVRUcH69etZuXIl+fn5zJs3b3DZFVdcwZ133smqVas455xzWLduXQ4rnT6Wq9ytq6tz9fX1OflsEcm+3bt3s3z58lyXESij7VMz2+qcqxttfd0pKiISEAp0EZGAUKCLiASEAl1EJCAU6CIiAaFAFxEJCAW6iJyRioqKAGhsbGTDhg2jrnPJJZcwUffq22+/nZ6ensH5XD6OV4EuIme0BQsWsHnz5im/f2Sg5/JxvAp0EQmEL3zhC8c9D/0rX/kKt956K5dddhlr167l/PPP5+GHHz7hffv27WPlypUA9Pb2snHjRlatWsX1119/3LNcbrzxRurq6lixYgW33HIL4D3wq7Gxkfe+9728973vBbzH8ba0eI+xuu2221i5ciUrV67k9ttvH/y85cuX8+lPf5oVK1bwvve9L2vPjNEfiRaR7HvsZjj8cna3Of98uPLrYy7euHEjn//85/nzP/9zAO6//35++ctf8pd/+ZeUlJTQ0tLCunXruOaaa8b882533HEHBQUF7Nixgx07drB27drBZV/72teYM2cO6XSayy67jB07dvC5z32O2267jS1btlBZWXnctrZu3cqPfvQjXnjhBZxzvPOd7+Q973kP5eXl0/aYXp2hi0ggrFmzhqamJhobG9m+fTvl5eVUV1fzpS99iVWrVnH55Zdz8OBBjhw5MuY2nnrqqcFgXbVqFatWrRpcdv/997N27VrWrFnDrl27eOWV8f/GzzPPPMN1111HYWEhRUVFfOhDH+Lpp58Gpu8xvTpDF5HsG+dMejpt2LCBzZs3c/jwYTZu3Mg999xDc3MzW7duJRqNUltbO+pjc4cb7ez9zTff5O///u958cUXKS8v54YbbphwO+M9J2u6HtOrM3QRCYyNGzdy7733snnzZjZs2EB7eztz584lGo2yZcsW9u/fP+77L774Yu655x4Adu7cyY4dOwDo6OigsLCQ0tJS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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.plot(history.history['loss'],label= 'train')\n",
    "plt.plot(history.history['val_loss'],label= 'validation')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WARNING:tensorflow:5 out of the last 5 calls to <function Model.make_predict_function.<locals>.predict_function at 0x0000011D052BE318> triggered tf.function retracing. Tracing is expensive and the excessive number of tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing tensors with different shapes, (3) passing Python objects instead of tensors. For (1), please define your @tf.function outside of the loop. For (2), @tf.function has experimental_relax_shapes=True option that relaxes argument shapes that can avoid unnecessary retracing. For (3), please refer to https://www.tensorflow.org/tutorials/customization/performance#python_or_tensor_args and https://www.tensorflow.org/api_docs/python/tf/function for  more details.\n"
     ]
    }
   ],
   "source": [
    "y_pred = model.predict(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_train_inv = cost_transformer.inverse_transform(y_train.reshape(1,-1))\n",
    "y_test_inv = cost_transformer.inverse_transform(y_test.reshape(1,-1))\n",
    "y_pred_inv = cost_transformer.inverse_transform(y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(y_test_inv.flatten(),marker = \".\",label = \"true\")\n",
    "plt.plot(y_pred_inv.flatten(),\"r\",label = \"Prediction\")\n",
    "plt.legend();"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
