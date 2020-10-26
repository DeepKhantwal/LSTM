{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on built-in function len in module builtins:\n",
      "\n",
      "len(obj, /)\n",
      "    Return the number of items in a container.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "len?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-14-cb2f59b8799d>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-14-cb2f59b8799d>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    Docstring: \"Multiple inputs given\"\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "def multiply(a,b):\n",
    "    c=a*b\n",
    "    return(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multiply(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "multiply??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Enter any alphabet or letter anf press tab to complete'''\n",
    "'''Beyond tab completion: Wildcard matching'''\n",
    "*Warning? \n",
    "\"we can use this to list every object in the namespace that ends withWarning\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "UsageError: Line magic function `%cpaste` not found.\n"
     ]
    }
   ],
   "source": [
    "%cpaste\n",
    "def donothing(x):\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print(In)\n",
    "#print(Out)\n",
    "#print(_)\n",
    "#print(__)\n",
    "'''The easiest way to suppress the output of a command is to add a semicolon\n",
    "to the end of the line'''\n",
    "\n",
    "import math\n",
    "math.sin(2) + math.cos(2);\n",
    "math.sin(2) + math.cos(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "> \u001b[1;32m<ipython-input-38-c0c8711c1747>\u001b[0m(6)\u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m      2 \u001b[1;33m\u001b[1;31m#print(Out)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0m\u001b[1;32m      3 \u001b[1;33m\u001b[1;31m#print(_)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0m\u001b[1;32m      4 \u001b[1;33m\u001b[1;31m#print(__)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0m\u001b[1;32m      5 \u001b[1;33m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0m\u001b[1;32m----> 6 \u001b[1;33m\u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msin\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcos\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[0m\n",
      "ipdb> print(a)\n",
      "*** NameError: name 'a' is not defined\n",
      "ipdb> quit\n"
     ]
    }
   ],
   "source": [
    "''' For debugging'''\n",
    "%debug\n",
    "\n",
    "'''Profiling and code execution timing and memory used by each line of code '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import numpy as np\n",
    "#numpy.__version__\n",
    "np."
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
