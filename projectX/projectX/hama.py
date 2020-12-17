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
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create the dataframe and upload your csv (dataframe with the variable name ham below)\n",
    "ham = pd.read_csv('qqqqOUTAGE HISTORY (All Columns).csv')"
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
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Site Name(Office)       Raised Time  \\\n",
      "0  Mabelreign-HA0228  12/14/2020 15:28   \n",
      "1    Zhombe-MD5202-U  12/13/2020 17:07   \n",
      "2    Zhombe-MD5202-U  12/13/2020 17:07   \n",
      "3    Zhombe-MD5202-U  12/13/2020 17:07   \n",
      "4    Zhombe-MD5202-U  12/13/2020 17:10   \n",
      "\n",
      "                                  Alarm Code      Cleared Time  \\\n",
      "0  Link between OMM and NE broken(198099803)  12/14/2020 15:31   \n",
      "1          Cell is out of service(199083022)  12/14/2020 15:25   \n",
      "2          Cell is out of service(199083022)  12/14/2020 15:25   \n",
      "3          Cell is out of service(199083022)  12/14/2020 15:25   \n",
      "4  Link between OMM and NE broken(198099803)  12/14/2020 15:23   \n",
      "\n",
      "  Duration(hh:mm:ss)  Severity                    NE              Alarm Type  \\\n",
      "0            0:02:32  Critical  Mabelreign-HA0228(8)    Communications Alarm   \n",
      "1           22:18:19  Critical      Harare V4 RNC(4)  Processing Error Alarm   \n",
      "2           22:18:19  Critical      Harare V4 RNC(4)  Processing Error Alarm   \n",
      "3           22:18:19  Critical      Harare V4 RNC(4)  Processing Error Alarm   \n",
      "4           22:12:39  Critical  Zhombe-MD5202-U(103)    Communications Alarm   \n",
      "\n",
      "   Root Alarm Indicator                                           Location  \\\n",
      "0                   NaN                                                NaN   \n",
      "1                   NaN  Global(V4)=1,Rack(V4)=1,Shelf(V4)=1,Board(V4)=...   \n",
      "2                   NaN  Global(V4)=1,Rack(V4)=1,Shelf(V4)=1,Board(V4)=...   \n",
      "3                   NaN  Global(V4)=1,Rack(V4)=1,Shelf(V4)=1,Board(V4)=...   \n",
      "4                   NaN                                                NaN   \n",
      "\n",
      "   ...        NE IP Link                            NE Group        NE Agent  \\\n",
      "0  ...  10.182.0.73  NaN    SDRMGR_V4 OMMB,Harare V4 OMMB(4)  SDRMGR_V4 OMMB   \n",
      "1  ...    129.0.1.1  NaN  Harare V4 RNC,TELCEL HAR V4 RNC(4)   Harare V4 RNC   \n",
      "2  ...    129.0.1.1  NaN  Harare V4 RNC,TELCEL HAR V4 RNC(4)   Harare V4 RNC   \n",
      "3  ...    129.0.1.1  NaN  Harare V4 RNC,TELCEL HAR V4 RNC(4)   Harare V4 RNC   \n",
      "4  ...  10.182.3.41  NaN    SDRMGR_V4 OMMB,Harare V4 OMMB(4)  SDRMGR_V4 OMMB   \n",
      "\n",
      "   Related Service(s) Create Type Threshold Information Maintenance State  \\\n",
      "0                 NaN         NaN                   NaN               NaN   \n",
      "1                 NaN         NaN                   NaN               NaN   \n",
      "2                 NaN         NaN                   NaN               NaN   \n",
      "3                 NaN         NaN                   NaN               NaN   \n",
      "4                 NaN         NaN                   NaN               NaN   \n",
      "\n",
      "   Raised Logging Time  Cleared Logging Time  \n",
      "0     12/14/2020 15:23      12/14/2020 15:26  \n",
      "1     12/13/2020 17:01      12/14/2020 15:20  \n",
      "2     12/13/2020 17:01      12/14/2020 15:20  \n",
      "3     12/13/2020 17:01      12/14/2020 15:20  \n",
      "4     12/13/2020 17:05      12/14/2020 15:17  \n",
      "\n",
      "[5 rows x 53 columns]\n"
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
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Site Name(Office)', 'Raised Time', 'Alarm Code', 'Cleared Time',\n",
      "       'Duration(hh:mm:ss)', 'Severity', 'NE', 'Alarm Type',\n",
      "       'Root Alarm Indicator', 'Location', 'NE Type', 'Specific Problem',\n",
      "       'Remark', 'ADMC Alarm', 'Repeated Count', 'Alarm Object Type',\n",
      "       'Alarm Object DN', 'Board Type', 'Alarm Object ID', 'Site ID(Office)',\n",
      "       'Alarm Object Name', 'ACK State', 'System Type', 'Probable Cause',\n",
      "       'Product', 'Alarm AID', 'Additional NE', 'Additional Location',\n",
      "       'Changed Time', 'Additional Information', '(Un)ACK User ID',\n",
      "       '(Un)ACK System ID', '(Un)ACK Time', '(Un)ACK Information',\n",
      "       'Clear User ID', 'Clear System ID', 'Clear Type', 'Clear Info',\n",
      "       'Comment', 'Comment User ID', 'Comment System ID', 'Comment Time',\n",
      "       'Alarm ID', 'NE IP', 'Link', 'NE Group', 'NE Agent',\n",
      "       'Related Service(s)', 'Create Type', 'Threshold Information',\n",
      "       'Maintenance State', 'Raised Logging Time', 'Cleared Logging Time'],\n",
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
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'CUST_NAME'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32mc:\\users\\hamat\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m   2894\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2895\u001b[1;33m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2896\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32mpandas\\_libs\\hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'CUST_NAME'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-45-0bbfe7bc8abb>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Reach a specific column\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mham\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'CUST_NAME'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m#just printing 1 column(s)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m#then again if you are lazy like me just type   print(ham.CUST_NAME)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m#You might want to print multiple specified columns its:   print(ham[['CUST_CODE','CUST_NAME']])\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\hamat\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   2904\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnlevels\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2905\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2906\u001b[1;33m             \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2907\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2908\u001b[0m                 \u001b[0mindexer\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0mindexer\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\hamat\\appdata\\local\\programs\\python\\python38\\lib\\site-packages\\pandas\\core\\indexes\\base.py\u001b[0m in \u001b[0;36mget_loc\u001b[1;34m(self, key, method, tolerance)\u001b[0m\n\u001b[0;32m   2895\u001b[0m                 \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcasted_key\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2896\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2897\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   2898\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2899\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mtolerance\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'CUST_NAME'"
     ]
    }
   ],
   "source": [
    "#Reach a specific column\n",
    "print(ham['CUST_NAME'][0:5])  #just printing 1 column(s)\n",
    "\n",
    "#then again if you are lazy like me just type   print(ham.CUST_NAME)\n",
    "#You might want to print multiple specified columns its:   print(ham[['CUST_CODE','CUST_NAME']])"
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
