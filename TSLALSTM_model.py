{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 250,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow import keras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\n",
    "  \"C:/Users/pradeep.kumar/Desktop/NLP/TSLA.csv\",\n",
    "  parse_dates=['Date'],\n",
    "  index_col=\"Date\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
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
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
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
       "      <td>2015-07-10</td>\n",
       "      <td>52.444000</td>\n",
       "      <td>52.599998</td>\n",
       "      <td>51.563999</td>\n",
       "      <td>51.830002</td>\n",
       "      <td>51.830002</td>\n",
       "      <td>13054500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-07-13</td>\n",
       "      <td>52.450001</td>\n",
       "      <td>52.509998</td>\n",
       "      <td>51.209999</td>\n",
       "      <td>52.431999</td>\n",
       "      <td>52.431999</td>\n",
       "      <td>14801500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-07-14</td>\n",
       "      <td>52.419998</td>\n",
       "      <td>53.198002</td>\n",
       "      <td>52.102001</td>\n",
       "      <td>53.130001</td>\n",
       "      <td>53.130001</td>\n",
       "      <td>9538000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-07-15</td>\n",
       "      <td>53.348000</td>\n",
       "      <td>53.498001</td>\n",
       "      <td>52.416000</td>\n",
       "      <td>52.627998</td>\n",
       "      <td>52.627998</td>\n",
       "      <td>10108000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2015-07-16</td>\n",
       "      <td>52.844002</td>\n",
       "      <td>53.439999</td>\n",
       "      <td>52.632000</td>\n",
       "      <td>53.335999</td>\n",
       "      <td>53.335999</td>\n",
       "      <td>8080000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Open       High        Low      Close  Adj Close    Volume\n",
       "Date                                                                       \n",
       "2015-07-10  52.444000  52.599998  51.563999  51.830002  51.830002  13054500\n",
       "2015-07-13  52.450001  52.509998  51.209999  52.431999  52.431999  14801500\n",
       "2015-07-14  52.419998  53.198002  52.102001  53.130001  53.130001   9538000\n",
       "2015-07-15  53.348000  53.498001  52.416000  52.627998  52.627998  10108000\n",
       "2015-07-16  52.844002  53.439999  52.632000  53.335999  53.335999   8080000"
      ]
     },
     "execution_count": 252,
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
   "execution_count": 253,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1259, 6)"
      ]
     },
     "execution_count": 253,
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
   "execution_count": 255,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11d059ff148>"
      ]
     },
     "execution_count": 255,
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
    "sns.lineplot(x=df.index,y='Close',data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x11d11ff3ac8>"
      ]
     },
     "execution_count": 256,
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
    "df_by_month = df.resample('M').sum()\n",
    "sns.lineplot(x=df_by_month.index,y='Close',data=df_by_month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1133\n",
      "126\n",
      "(1133, 6) (126, 6)\n"
     ]
    }
   ],
   "source": [
    "train_size = int(len(df)*0.9)\n",
    "test_size = len(df) - train_size\n",
    "print(train_size)\n",
    "print(test_size)\n",
    "train,test = df.iloc[0:train_size,:],df.iloc[train_size:len(df),:]\n",
    "print(train.shape,test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scaling Data for passing LSTM \n",
    "from sklearn.preprocessing import RobustScaler\n",
    "\n",
    "f_columns = [\"Open\", \"High\", \"Low\",\"Adj Close\",\"Volume\"]\n",
    "f_cost = [\"Close\"]\n",
    "\n",
    "f_transformer = RobustScaler()\n",
    "cost_transformer = RobustScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [],
   "source": [
    "f_transformer = f_transformer.fit(train[f_columns].to_numpy())\n",
    "cost_transformer = cost_transformer.fit(train[f_cost])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
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
   "execution_count": 261,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create dataset for LSTM format\n",
    "import numpy as np\n",
    "def create_dataset(X,y,time_steps=1):\n",
    "    Xs,ys = [],[]\n",
    "    for i in range(len(X) - time_steps):\n",
    "        v = X.iloc[i:(i + time_steps),:].to_numpy()\n",
    "        Xs.append(v)\n",
    "        ys.append(y.iloc[i + time_steps])\n",
    "    return np.array(Xs),np.array(ys)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 278,
   "metadata": {},
   "outputs": [],
   "source": [
    "TIME_STEPS = 60\n",
    "X_train, y_train = create_dataset(train, train.Volume, time_steps = TIME_STEPS)\n",
    "X_test, y_test = create_dataset(test, test.Volume, time_steps = TIME_STEPS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1073, 60, 6) (1073,)\n"
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
   "execution_count": 280,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(66, 60, 6) (66,)\n"
     ]
    }
   ],
   "source": [
    "print(X_test.shape,y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
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
   "execution_count": 287,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/100\n",
      "27/27 [==============================] - 1s 54ms/step - loss: 0.6128 - val_loss: 1.2185\n",
      "Epoch 2/100\n",
      "27/27 [==============================] - 1s 51ms/step - loss: 0.5951 - val_loss: 1.2266\n",
      "Epoch 3/100\n",
      "27/27 [==============================] - 1s 51ms/step - loss: 0.5849 - val_loss: 1.2437\n",
      "Epoch 4/100\n",
      "27/27 [==============================] - 1s 49ms/step - loss: 0.5964 - val_loss: 1.2689\n",
      "Epoch 5/100\n",
      "27/27 [==============================] - 1s 49ms/step - loss: 0.6122 - val_loss: 1.2417\n",
      "Epoch 6/100\n",
      "27/27 [==============================] - 2s 60ms/step - loss: 0.5743 - val_loss: 1.2067\n",
      "Epoch 7/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.5678 - val_loss: 1.1845\n",
      "Epoch 8/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5483 - val_loss: 1.1972\n",
      "Epoch 9/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5517 - val_loss: 1.1840\n",
      "Epoch 10/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5502 - val_loss: 1.2069\n",
      "Epoch 11/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5620 - val_loss: 1.2145\n",
      "Epoch 12/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.5514 - val_loss: 1.2025\n",
      "Epoch 13/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5565 - val_loss: 1.2014\n",
      "Epoch 14/100\n",
      "27/27 [==============================] - 2s 67ms/step - loss: 0.5333 - val_loss: 1.3493\n",
      "Epoch 15/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5282 - val_loss: 1.3721\n",
      "Epoch 16/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5377 - val_loss: 1.2563\n",
      "Epoch 17/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5732 - val_loss: 1.2283\n",
      "Epoch 18/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5697 - val_loss: 1.2500\n",
      "Epoch 19/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.5511 - val_loss: 1.2267\n",
      "Epoch 20/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.5540 - val_loss: 1.2319\n",
      "Epoch 21/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.5323 - val_loss: 1.2124\n",
      "Epoch 22/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.5316 - val_loss: 1.2379\n",
      "Epoch 23/100\n",
      "27/27 [==============================] - 2s 76ms/step - loss: 0.5322 - val_loss: 1.2845\n",
      "Epoch 24/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.5277 - val_loss: 1.2414\n",
      "Epoch 25/100\n",
      "27/27 [==============================] - 2s 78ms/step - loss: 0.5325 - val_loss: 1.2577\n",
      "Epoch 26/100\n",
      "27/27 [==============================] - 2s 75ms/step - loss: 0.5169 - val_loss: 1.2554\n",
      "Epoch 27/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.5134 - val_loss: 1.3307\n",
      "Epoch 28/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5291 - val_loss: 1.2105\n",
      "Epoch 29/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5386 - val_loss: 1.2081\n",
      "Epoch 30/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5282 - val_loss: 1.2376\n",
      "Epoch 31/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.5210 - val_loss: 1.2730\n",
      "Epoch 32/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4837 - val_loss: 1.3365\n",
      "Epoch 33/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4700 - val_loss: 1.4817\n",
      "Epoch 34/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5040 - val_loss: 1.4353\n",
      "Epoch 35/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5452 - val_loss: 1.3017\n",
      "Epoch 36/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.5249 - val_loss: 1.2492\n",
      "Epoch 37/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5013 - val_loss: 1.2831\n",
      "Epoch 38/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4943 - val_loss: 1.3669\n",
      "Epoch 39/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4879 - val_loss: 1.5300\n",
      "Epoch 40/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5584 - val_loss: 1.4375\n",
      "Epoch 41/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5154 - val_loss: 1.4299\n",
      "Epoch 42/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5140 - val_loss: 1.4376\n",
      "Epoch 43/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.5078 - val_loss: 1.4179\n",
      "Epoch 44/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.5132 - val_loss: 1.4488\n",
      "Epoch 45/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.4845 - val_loss: 1.4637\n",
      "Epoch 46/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.4612 - val_loss: 1.3904\n",
      "Epoch 47/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.4488 - val_loss: 1.3722\n",
      "Epoch 48/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.5002 - val_loss: 1.4423\n",
      "Epoch 49/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4945 - val_loss: 1.3968\n",
      "Epoch 50/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4870 - val_loss: 1.3761\n",
      "Epoch 51/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.4864 - val_loss: 1.4179\n",
      "Epoch 52/100\n",
      "27/27 [==============================] - 2s 68ms/step - loss: 0.4536 - val_loss: 1.4457\n",
      "Epoch 53/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4720 - val_loss: 1.4158\n",
      "Epoch 54/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.5174 - val_loss: 1.4330\n",
      "Epoch 55/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.5319 - val_loss: 1.3013\n",
      "Epoch 56/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.5173 - val_loss: 1.3828\n",
      "Epoch 57/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.4780 - val_loss: 1.4189\n",
      "Epoch 58/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4754 - val_loss: 1.4657\n",
      "Epoch 59/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4536 - val_loss: 1.4947\n",
      "Epoch 60/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4397 - val_loss: 1.5596\n",
      "Epoch 61/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4649 - val_loss: 1.5732\n",
      "Epoch 62/100\n",
      "27/27 [==============================] - 2s 78ms/step - loss: 0.4928 - val_loss: 1.3367\n",
      "Epoch 63/100\n",
      "27/27 [==============================] - 2s 81ms/step - loss: 0.4433 - val_loss: 1.3745\n",
      "Epoch 64/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4268 - val_loss: 1.5488\n",
      "Epoch 65/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4597 - val_loss: 1.5251\n",
      "Epoch 66/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.4250 - val_loss: 1.5603\n",
      "Epoch 67/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4180 - val_loss: 1.5298\n",
      "Epoch 68/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4423 - val_loss: 1.4507\n",
      "Epoch 69/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4682 - val_loss: 1.4912\n",
      "Epoch 70/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.4754 - val_loss: 1.5045\n",
      "Epoch 71/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.4382 - val_loss: 1.5221\n",
      "Epoch 72/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4196 - val_loss: 1.4212\n",
      "Epoch 73/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.4102 - val_loss: 1.6547\n",
      "Epoch 74/100\n",
      "27/27 [==============================] - 2s 78ms/step - loss: 0.4123 - val_loss: 1.5146\n",
      "Epoch 75/100\n",
      "27/27 [==============================] - 2s 76ms/step - loss: 0.4201 - val_loss: 1.4629\n",
      "Epoch 76/100\n",
      "27/27 [==============================] - 2s 70ms/step - loss: 0.4369 - val_loss: 1.4987\n",
      "Epoch 77/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.4116 - val_loss: 1.3736\n",
      "Epoch 78/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.4396 - val_loss: 1.4427\n",
      "Epoch 79/100\n",
      "27/27 [==============================] - 2s 80ms/step - loss: 0.3897 - val_loss: 1.4762\n",
      "Epoch 80/100\n",
      "27/27 [==============================] - 2s 79ms/step - loss: 0.4099 - val_loss: 1.4869\n",
      "Epoch 81/100\n",
      "27/27 [==============================] - 2s 82ms/step - loss: 0.3906 - val_loss: 1.4427\n",
      "Epoch 82/100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27/27 [==============================] - 2s 75ms/step - loss: 0.3728 - val_loss: 1.4641\n",
      "Epoch 83/100\n",
      "27/27 [==============================] - 2s 83ms/step - loss: 0.3652 - val_loss: 1.4932\n",
      "Epoch 84/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.3588 - val_loss: 1.5268\n",
      "Epoch 85/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.3557 - val_loss: 1.5035\n",
      "Epoch 86/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.4021 - val_loss: 1.7816\n",
      "Epoch 87/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.3943 - val_loss: 1.5788\n",
      "Epoch 88/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.3692 - val_loss: 1.6847\n",
      "Epoch 89/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.3704 - val_loss: 1.5240\n",
      "Epoch 90/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.3531 - val_loss: 1.5004\n",
      "Epoch 91/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.3414 - val_loss: 1.4943\n",
      "Epoch 92/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.3392 - val_loss: 1.5086\n",
      "Epoch 93/100\n",
      "27/27 [==============================] - 2s 69ms/step - loss: 0.3335 - val_loss: 1.5753\n",
      "Epoch 94/100\n",
      "27/27 [==============================] - 2s 71ms/step - loss: 0.3125 - val_loss: 1.6314\n",
      "Epoch 95/100\n",
      "27/27 [==============================] - 2s 77ms/step - loss: 0.3008 - val_loss: 1.5852\n",
      "Epoch 96/100\n",
      "27/27 [==============================] - 2s 76ms/step - loss: 0.3025 - val_loss: 1.6880\n",
      "Epoch 97/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.2942 - val_loss: 1.6867\n",
      "Epoch 98/100\n",
      "27/27 [==============================] - 2s 74ms/step - loss: 0.3482 - val_loss: 1.6178\n",
      "Epoch 99/100\n",
      "27/27 [==============================] - 2s 72ms/step - loss: 0.3952 - val_loss: 1.5900\n",
      "Epoch 100/100\n",
      "27/27 [==============================] - 2s 73ms/step - loss: 0.4544 - val_loss: 1.4570\n"
     ]
    }
   ],
   "source": [
    "history = model.fit(\n",
    "    X_train, y_train,\n",
    "    epochs=100,\n",
    "    batch_size=32,\n",
    "    validation_split=0.2,\n",
    "    shuffle=False\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
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
    "import matplotlib.pyplot as plt\n",
    "plt.plot(history.history['loss'],label= 'train')\n",
    "plt.plot(history.history['val_loss'],label= 'validation')\n",
    "plt.legend();"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 295,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
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
   "execution_count": 297,
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
    "plt.plot(y_pred_inv.flatten(),label = \"Prediction\")\n",
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
