{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "LOADIND DATA INTO PANDAS (PUT YOUR DATA IN A DATAFRAME) Such that it is easily manipulated"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the pandas library\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\hamat\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3146: DtypeWarning: Columns (5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) have mixed types.Specify dtype option on import or set low_memory=False.\n",
      "  has_raised = await self.run_ast_nodes(code_ast.body, cell_name,\n"
     ]
    }
   ],
   "source": [
    "#create the dataframe and upload your csv (dataframe with the variable name ham below)\n",
    "ham = pd.read_csv('billing_report_August2020.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NOTE: Dataset is big so you might have a red error saying set low_memory=False, as of now just ignore it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  CUST_CODE                                   CUST_NAME       ACC_NBR  \\\n",
      "0    SOL006  TRAC - KING (PRIVATE LIMITED) (SMS  ONLY )  2.637325e+11   \n",
      "1    SOL006  TRAC - KING (PRIVATE LIMITED) (SMS  ONLY )  2.637325e+11   \n",
      "2    AMT002                                 AMTRAK HIRE  2.637335e+11   \n",
      "3    SOL006  TRAC - KING (PRIVATE LIMITED) (SMS  ONLY )  2.637325e+11   \n",
      "4    SOL006  TRAC - KING (PRIVATE LIMITED) (SMS  ONLY )  2.637325e+11   \n",
      "\n",
      "       PRICE_PLAN_NAME  SUBS_ID RECURRING_FEE TELEMUNE     SMC  \\\n",
      "0  Club Senior Default   1144.0             0        0    0.99   \n",
      "1  Club Senior Default   1323.0             0        0    1.98   \n",
      "2  Televantage Default   1335.0          5.22        0  66.936   \n",
      "3  Club Senior Default   1434.0             0        0    1.98   \n",
      "4  Club Senior Default   1910.0             0        0    1.65   \n",
      "\n",
      "  TELECEL_TO_ECONET INTERNATIONAL  ... TELECEL_TO_NETONE TELECEL_TO_TELONE  \\\n",
      "0                 0             0  ...                 0                 0   \n",
      "1                 0             0  ...                 0                 0   \n",
      "2           15.5949             0  ...           10.4387            0.3109   \n",
      "3                 0             0  ...                 0                 0   \n",
      "4                 0             0  ...                 0                 0   \n",
      "\n",
      "  TELECEL_TO_POWERTEL ROAMING  TELECEL  LIQUID DISCOUNT TOTAL B4 TAX      TAX  \\\n",
      "0                   0       0        0       0        0         0.99  0.14355   \n",
      "1                   0       0        0       0        0         1.98   0.2871   \n",
      "2                   0       0  17.2129  0.6089        0      116.322  16.8667   \n",
      "3                   0       0        0       0        0         1.98   0.2871   \n",
      "4                   0       0        0       0        0         1.65  0.23925   \n",
      "\n",
      "     TOTAL  \n",
      "0  1.13355  \n",
      "1   2.2671  \n",
      "2  133.189  \n",
      "3   2.2671  \n",
      "4  1.88925  \n",
      "\n",
      "[5 rows x 21 columns]\n"
     ]
    }
   ],
   "source": [
    "#just print your dataset to know if its loaded. not important but just playing around. Printin the top 5 rows\n",
    "print(ham.head(5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you have successfuly run that then let the real code begin, we have successfuly accessed our CSV Billing file. In case maybe you want to print out the bottom rows just to confirm if it's the real CVS that you are using, use the code below\n",
    "\n",
    "-> print (ham.tail(->insert the number of rows you wanted to be printed out here)\n",
    "\n",
    "NOTE: Sometimes you would'nt want to change the file path, the Billing excel file has been changed from it's original format which is \".xlsx\" to \".csv\" so Instead if you are lazy like me cause next time i won't change it on creating the DATAFRAME on the second line you type:\n",
    "\n",
    "ham = pd.read_excel('billing_report_August2020.xlsx')\n",
    "\n",
    "\n",
    "Note also, the variable name \"ham\" is of your own choice and you can as many DataFrames as you want, instead of \"ham\" you could even write \"telecel\" whichever name you can just refer to."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "READING DATA IN PANDAS\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['CUST_CODE', 'CUST_NAME', 'ACC_NBR', 'PRICE_PLAN_NAME', 'SUBS_ID',\n",
      "       'RECURRING_FEE', 'TELEMUNE', 'SMC', 'TELECEL_TO_ECONET',\n",
      "       'INTERNATIONAL', 'TELECEL_TO_AFRICOM', 'TELECEL_TO_NETONE',\n",
      "       'TELECEL_TO_TELONE', 'TELECEL_TO_POWERTEL', 'ROAMING', 'TELECEL',\n",
      "       'LIQUID', 'DISCOUNT', 'TOTAL B4 TAX', 'TAX', 'TOTAL'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "#Reading Headers (Column names)\n",
    "print(ham.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NOTE: IN OUR CASE THIS MIGHT BE IMPORTANT BECAUSE WE WANT TO PLAY AROUND WITH CERTAIN SPECIFIC COLUMNS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
