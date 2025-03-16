{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fb371f13",
   "metadata": {
    "papermill": {
     "duration": 0.007314,
     "end_time": "2025-03-16T22:20:10.146002",
     "exception": false,
     "start_time": "2025-03-16T22:20:10.138688",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**This notebook is an exercise in the [Python](https://www.kaggle.com/learn/python) course.  You can reference the tutorial at [this link](https://www.kaggle.com/colinmorris/booleans-and-conditionals).**\n",
    "\n",
    "---\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2c70a75",
   "metadata": {
    "papermill": {
     "duration": 0.006859,
     "end_time": "2025-03-16T22:20:10.159791",
     "exception": false,
     "start_time": "2025-03-16T22:20:10.152932",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "In this exercise, you'll put to work what you have learned about booleans and conditionals.\n",
    "\n",
    "To get started, **run the setup code below** before writing your own code (and if you leave this notebook and come back later, don't forget to run the setup code again)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5daed643",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:10.175248Z",
     "iopub.status.busy": "2025-03-16T22:20:10.174709Z",
     "iopub.status.idle": "2025-03-16T22:20:11.382669Z",
     "shell.execute_reply": "2025-03-16T22:20:11.381304Z"
    },
    "papermill": {
     "duration": 1.218001,
     "end_time": "2025-03-16T22:20:11.384686",
     "exception": false,
     "start_time": "2025-03-16T22:20:10.166685",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup complete.\n"
     ]
    }
   ],
   "source": [
    "from learntools.core import binder; binder.bind(globals())\n",
    "from learntools.python.ex3 import *\n",
    "print('Setup complete.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db8e341a",
   "metadata": {
    "papermill": {
     "duration": 0.00659,
     "end_time": "2025-03-16T22:20:11.398547",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.391957",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 1.\n",
    "\n",
    "Many programming languages have [`sign`](https://en.wikipedia.org/wiki/Sign_function) available as a built-in function. Python doesn't, but we can define our own!\n",
    "\n",
    "In the cell below, define a function called `sign` which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ffff224e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.413182Z",
     "iopub.status.busy": "2025-03-16T22:20:11.412602Z",
     "iopub.status.idle": "2025-03-16T22:20:11.421894Z",
     "shell.execute_reply": "2025-03-16T22:20:11.420822Z"
    },
    "papermill": {
     "duration": 0.018425,
     "end_time": "2025-03-16T22:20:11.423606",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.405181",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"1_SignFunctionProblem\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Your code goes here. Define a function called 'sign'\n",
    "def sign(num):\n",
    "    if (num <0):\n",
    "        return -1\n",
    "    elif (num >0):\n",
    "        return 1\n",
    "    elif (num==0):\n",
    "        return 0\n",
    "# Check your answer\n",
    "q1.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a1f185af",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.439593Z",
     "iopub.status.busy": "2025-03-16T22:20:11.439236Z",
     "iopub.status.idle": "2025-03-16T22:20:11.443393Z",
     "shell.execute_reply": "2025-03-16T22:20:11.442333Z"
    },
    "papermill": {
     "duration": 0.013805,
     "end_time": "2025-03-16T22:20:11.445066",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.431261",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q1.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8a41a85",
   "metadata": {
    "papermill": {
     "duration": 0.006886,
     "end_time": "2025-03-16T22:20:11.459403",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.452517",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 2.\n",
    "\n",
    "We've decided to add \"logging\" to our `to_smash` function from the previous exercise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "096659c4",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.474696Z",
     "iopub.status.busy": "2025-03-16T22:20:11.474330Z",
     "iopub.status.idle": "2025-03-16T22:20:11.481524Z",
     "shell.execute_reply": "2025-03-16T22:20:11.480418Z"
    },
    "papermill": {
     "duration": 0.016827,
     "end_time": "2025-03-16T22:20:11.483307",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.466480",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Splitting 91 candies\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def to_smash(total_candies):\n",
    "    \"\"\"Return the number of leftover candies that must be smashed after distributing\n",
    "    the given number of candies evenly between 3 friends.\n",
    "    \n",
    "    >>> to_smash(91)\n",
    "    1\n",
    "    \"\"\"\n",
    "    print(\"Splitting\", total_candies, \"candies\")\n",
    "    return total_candies % 3\n",
    "\n",
    "to_smash(91)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f058e0d",
   "metadata": {
    "papermill": {
     "duration": 0.007265,
     "end_time": "2025-03-16T22:20:11.498283",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.491018",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "What happens if we call it with `total_candies = 1`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d64824f5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.514546Z",
     "iopub.status.busy": "2025-03-16T22:20:11.514197Z",
     "iopub.status.idle": "2025-03-16T22:20:11.520854Z",
     "shell.execute_reply": "2025-03-16T22:20:11.519730Z"
    },
    "papermill": {
     "duration": 0.016699,
     "end_time": "2025-03-16T22:20:11.522478",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.505779",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Splitting 1 candies\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "to_smash(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81a19861",
   "metadata": {
    "papermill": {
     "duration": 0.007505,
     "end_time": "2025-03-16T22:20:11.537710",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.530205",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "That isn't great grammar!\n",
    "\n",
    "Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular \"candy\" instead of the plural \"candies\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2bdb080b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.553747Z",
     "iopub.status.busy": "2025-03-16T22:20:11.553422Z",
     "iopub.status.idle": "2025-03-16T22:20:11.561780Z",
     "shell.execute_reply": "2025-03-16T22:20:11.560955Z"
    },
    "papermill": {
     "duration": 0.01828,
     "end_time": "2025-03-16T22:20:11.563482",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.545202",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Splitting 91  candies\n",
      "Splitting 1  candy\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def to_smash(total_candies):\n",
    "    \"\"\"Return the number of leftover candies that must be smashed after distributing\n",
    "    the given number of candies evenly between 3 friends.\n",
    "    \n",
    "    >>> to_smash(91)\n",
    "    1\n",
    "    \"\"\"\n",
    "    if (total_candies >1):\n",
    "        print(\"Splitting\", total_candies, \" candies\")\n",
    "    elif (total_candies == 1):\n",
    "        print(\"Splitting\", total_candies, \" candy\")\n",
    "    return total_candies % 3\n",
    "\n",
    "to_smash(91)\n",
    "to_smash(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4746574c",
   "metadata": {
    "papermill": {
     "duration": 0.007697,
     "end_time": "2025-03-16T22:20:11.579017",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.571320",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "To get credit for completing this problem, and to see the official answer, run the code cell below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9d919635",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.596320Z",
     "iopub.status.busy": "2025-03-16T22:20:11.595891Z",
     "iopub.status.idle": "2025-03-16T22:20:11.603425Z",
     "shell.execute_reply": "2025-03-16T22:20:11.602311Z"
    },
    "papermill": {
     "duration": 0.018018,
     "end_time": "2025-03-16T22:20:11.605247",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.587229",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 4, \"questionId\": \"2_PluralizationProblem\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> A straightforward (and totally fine) solution is to replace the original `print` call with:\n",
       "\n",
       "```python\n",
       "if total_candies == 1:\n",
       "    print(\"Splitting 1 candy\")\n",
       "else:\n",
       "    print(\"Splitting\", total_candies, \"candies\")\n",
       "```\n",
       "\n",
       "Here's a slightly more succinct solution using a conditional expression:\n",
       "\n",
       "```python\n",
       "print(\"Splitting\", total_candies, \"candy\" if total_candies == 1 else \"candies\")\n",
       "```"
      ],
      "text/plain": [
       "Solution: A straightforward (and totally fine) solution is to replace the original `print` call with:\n",
       "\n",
       "```python\n",
       "if total_candies == 1:\n",
       "    print(\"Splitting 1 candy\")\n",
       "else:\n",
       "    print(\"Splitting\", total_candies, \"candies\")\n",
       "```\n",
       "\n",
       "Here's a slightly more succinct solution using a conditional expression:\n",
       "\n",
       "```python\n",
       "print(\"Splitting\", total_candies, \"candy\" if total_candies == 1 else \"candies\")\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Check your answer (Run this code cell to receive credit!)\n",
    "q2.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e999702",
   "metadata": {
    "papermill": {
     "duration": 0.008117,
     "end_time": "2025-03-16T22:20:11.621538",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.613421",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 3. <span title=\"A bit spicy\" style=\"color: darkgreen \">🌶️</span>\n",
    "\n",
    "In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...\n",
    "- I have an umbrella...\n",
    "- or if the rain isn't too heavy and I have a hood...\n",
    "- otherwise, I'm still fine unless it's raining *and* it's a workday\n",
    "\n",
    "The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?\n",
    "\n",
    "To prove that `prepared_for_weather` is buggy, come up with a set of inputs where either:\n",
    "- the function returns `False` (but should have returned `True`), or\n",
    "- the function returned `True` (but should have returned `False`).\n",
    "\n",
    "To get credit for completing this question, your code should return a <font color='#33cc33'>Correct</font> result."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "da7da965",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.638304Z",
     "iopub.status.busy": "2025-03-16T22:20:11.637895Z",
     "iopub.status.idle": "2025-03-16T22:20:11.647783Z",
     "shell.execute_reply": "2025-03-16T22:20:11.646635Z"
    },
    "papermill": {
     "duration": 0.020194,
     "end_time": "2025-03-16T22:20:11.649475",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.629281",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 1, \"questionId\": \"3_WeatherDebug\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct:</span> \n",
       "\n",
       "One example of a failing test case is:\n",
       "\n",
       "```python\n",
       "have_umbrella = False\n",
       "rain_level = 0.0\n",
       "have_hood = False\n",
       "is_workday = False\n",
       "```\n",
       "\n",
       "Clearly we're prepared for the weather in this case. It's not raining. Not only that, it's not a workday, so we don't even need to leave the house! But our function will return False on these inputs.\n",
       "\n",
       "The key problem is that Python implictly parenthesizes the last part as:\n",
       "\n",
       "```python\n",
       "(not (rain_level > 0)) and is_workday\n",
       "```\n",
       "\n",
       "Whereas what we were trying to express would look more like:\n",
       "\n",
       "```python\n",
       "not (rain_level > 0 and is_workday)\n",
       "```\n"
      ],
      "text/plain": [
       "Correct: \n",
       "\n",
       "One example of a failing test case is:\n",
       "\n",
       "```python\n",
       "have_umbrella = False\n",
       "rain_level = 0.0\n",
       "have_hood = False\n",
       "is_workday = False\n",
       "```\n",
       "\n",
       "Clearly we're prepared for the weather in this case. It's not raining. Not only that, it's not a workday, so we don't even need to leave the house! But our function will return False on these inputs.\n",
       "\n",
       "The key problem is that Python implictly parenthesizes the last part as:\n",
       "\n",
       "```python\n",
       "(not (rain_level > 0)) and is_workday\n",
       "```\n",
       "\n",
       "Whereas what we were trying to express would look more like:\n",
       "\n",
       "```python\n",
       "not (rain_level > 0 and is_workday)\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):\n",
    "    # Don't change this code. Our goal is just to find the bug, not fix it!\n",
    "    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday\n",
    "\n",
    "# Change the values of these inputs so they represent a case where prepared_for_weather\n",
    "# returns the wrong answer.\n",
    "have_umbrella = False\n",
    "rain_level = 6.0\n",
    "have_hood = False\n",
    "is_workday = False\n",
    "\n",
    "# Check what the function returns given the current values of the variables above\n",
    "actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)\n",
    "print(actual)\n",
    "\n",
    "# Check your answer\n",
    "q3.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "41746524",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.667239Z",
     "iopub.status.busy": "2025-03-16T22:20:11.666850Z",
     "iopub.status.idle": "2025-03-16T22:20:11.670634Z",
     "shell.execute_reply": "2025-03-16T22:20:11.669730Z"
    },
    "papermill": {
     "duration": 0.014474,
     "end_time": "2025-03-16T22:20:11.672429",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.657955",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q3.hint()\n",
    "#q3.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b0c94c5",
   "metadata": {
    "papermill": {
     "duration": 0.007777,
     "end_time": "2025-03-16T22:20:11.688790",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.681013",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 4.\n",
    "\n",
    "The function `is_negative` below is implemented correctly - it returns True if the given number is negative and False otherwise.\n",
    "\n",
    "However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by *75%* while keeping the same behaviour. \n",
    "\n",
    "See if you can come up with an equivalent body that uses just **one line** of code, and put it in the function `concise_is_negative`. (HINT: you don't even need Python's ternary syntax)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "516d68df",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.706889Z",
     "iopub.status.busy": "2025-03-16T22:20:11.706547Z",
     "iopub.status.idle": "2025-03-16T22:20:11.714628Z",
     "shell.execute_reply": "2025-03-16T22:20:11.713555Z"
    },
    "papermill": {
     "duration": 0.019138,
     "end_time": "2025-03-16T22:20:11.716262",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.697124",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"4_ConciseIsNegative\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def is_negative(number):\n",
    "    if number < 0:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "def concise_is_negative(number):\n",
    "    pass # Your code goes here (try to keep it to one line!)\n",
    "    return (number < 0)\n",
    "# Check your answer\n",
    "q4.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "133ea984",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.734472Z",
     "iopub.status.busy": "2025-03-16T22:20:11.734112Z",
     "iopub.status.idle": "2025-03-16T22:20:11.738196Z",
     "shell.execute_reply": "2025-03-16T22:20:11.737009Z"
    },
    "papermill": {
     "duration": 0.015068,
     "end_time": "2025-03-16T22:20:11.739873",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.724805",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q4.hint()\n",
    "#q4.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "836bc0a3",
   "metadata": {
    "papermill": {
     "duration": 0.008169,
     "end_time": "2025-03-16T22:20:11.756810",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.748641",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 5a.\n",
    "\n",
    "The boolean variables `ketchup`, `mustard` and `onion` represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "500dccfa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.775996Z",
     "iopub.status.busy": "2025-03-16T22:20:11.775639Z",
     "iopub.status.idle": "2025-03-16T22:20:11.780104Z",
     "shell.execute_reply": "2025-03-16T22:20:11.779011Z"
    },
    "papermill": {
     "duration": 0.015455,
     "end_time": "2025-03-16T22:20:11.781768",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.766313",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def onionless(ketchup, mustard, onion):\n",
    "    \"\"\"Return whether the customer doesn't want onions.\n",
    "    \"\"\"\n",
    "    return not onion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0591aca5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.799872Z",
     "iopub.status.busy": "2025-03-16T22:20:11.799533Z",
     "iopub.status.idle": "2025-03-16T22:20:11.807809Z",
     "shell.execute_reply": "2025-03-16T22:20:11.806743Z"
    },
    "papermill": {
     "duration": 0.019196,
     "end_time": "2025-03-16T22:20:11.809543",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.790347",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"5.1_AllToppings\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def wants_all_toppings(ketchup, mustard, onion):\n",
    "    \"\"\"Return whether the customer wants \"the works\" (all 3 toppings)\n",
    "    \"\"\"\n",
    "    pass\n",
    "    return ketchup and mustard and onion\n",
    "# Check your answer\n",
    "q5.a.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "61c0e3e0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.830556Z",
     "iopub.status.busy": "2025-03-16T22:20:11.830140Z",
     "iopub.status.idle": "2025-03-16T22:20:11.834345Z",
     "shell.execute_reply": "2025-03-16T22:20:11.833266Z"
    },
    "papermill": {
     "duration": 0.015804,
     "end_time": "2025-03-16T22:20:11.836091",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.820287",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q5.a.hint()\n",
    "#q5.a.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f3e7afd1",
   "metadata": {
    "papermill": {
     "duration": 0.008422,
     "end_time": "2025-03-16T22:20:11.853665",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.845243",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 5b.\n",
    "\n",
    "For the next function, fill in the body to match the English description in the docstring. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "683b332e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.872913Z",
     "iopub.status.busy": "2025-03-16T22:20:11.872526Z",
     "iopub.status.idle": "2025-03-16T22:20:11.881246Z",
     "shell.execute_reply": "2025-03-16T22:20:11.880053Z"
    },
    "papermill": {
     "duration": 0.020551,
     "end_time": "2025-03-16T22:20:11.883060",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.862509",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"5.2_PlainDog\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct:</span> \n",
       "\n",
       "One solution looks like:\n",
       "```python\n",
       "return not ketchup and not mustard and not onion\n",
       "```\n",
       "\n",
       "We can also [\"factor out\" the nots](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) to get:\n",
       "\n",
       "```python\n",
       "return not (ketchup or mustard or onion)\n",
       "```"
      ],
      "text/plain": [
       "Correct: \n",
       "\n",
       "One solution looks like:\n",
       "```python\n",
       "return not ketchup and not mustard and not onion\n",
       "```\n",
       "\n",
       "We can also [\"factor out\" the nots](https://en.wikipedia.org/wiki/De_Morgan%27s_laws) to get:\n",
       "\n",
       "```python\n",
       "return not (ketchup or mustard or onion)\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def wants_plain_hotdog(ketchup, mustard, onion):\n",
    "    \"\"\"Return whether the customer wants a plain hot dog with no toppings.\n",
    "    \"\"\"\n",
    "    pass\n",
    "    return not (ketchup or mustard or onion)\n",
    "\n",
    "# Check your answer\n",
    "q5.b.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1c4aff99",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.903351Z",
     "iopub.status.busy": "2025-03-16T22:20:11.902930Z",
     "iopub.status.idle": "2025-03-16T22:20:11.907220Z",
     "shell.execute_reply": "2025-03-16T22:20:11.905792Z"
    },
    "papermill": {
     "duration": 0.016479,
     "end_time": "2025-03-16T22:20:11.909126",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.892647",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q5.b.hint()\n",
    "#q5.b.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d81202d",
   "metadata": {
    "papermill": {
     "duration": 0.008854,
     "end_time": "2025-03-16T22:20:11.927495",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.918641",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 5c.\n",
    "\n",
    "You know what to do: for the next function, fill in the body to match the English description in the docstring."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "189dbeaa",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.947092Z",
     "iopub.status.busy": "2025-03-16T22:20:11.946759Z",
     "iopub.status.idle": "2025-03-16T22:20:11.954825Z",
     "shell.execute_reply": "2025-03-16T22:20:11.953772Z"
    },
    "papermill": {
     "duration": 0.02004,
     "end_time": "2025-03-16T22:20:11.956674",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.936634",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"5.3_OneSauce\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct</span>"
      ],
      "text/plain": [
       "Correct"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def exactly_one_sauce(ketchup, mustard, onion):\n",
    "    \"\"\"Return whether the customer wants either ketchup or mustard, but not both.\n",
    "    (You may be familiar with this operation under the name \"exclusive or\")\n",
    "    \"\"\"\n",
    "    pass\n",
    "    return ((ketchup and not mustard ) or  (not ketchup and mustard))\n",
    "\n",
    "# Check your answer\n",
    "q5.c.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "8f17b37c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:11.976742Z",
     "iopub.status.busy": "2025-03-16T22:20:11.976420Z",
     "iopub.status.idle": "2025-03-16T22:20:11.986928Z",
     "shell.execute_reply": "2025-03-16T22:20:11.986035Z"
    },
    "papermill": {
     "duration": 0.022463,
     "end_time": "2025-03-16T22:20:11.988522",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.966059",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 2, \"questionType\": 2, \"questionId\": \"5.3_OneSauce\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#3366cc\">Hint:</span> There are exactly two ways to set ketchup and mustard to make this true. What are they?"
      ],
      "text/plain": [
       "Hint: There are exactly two ways to set ketchup and mustard to make this true. What are they?"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"interactionType\": 3, \"questionType\": 2, \"questionId\": \"5.3_OneSauce\", \"learnToolsVersion\": \"0.3.4\", \"valueTowardsCompletion\": 0.0, \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\", \"outcomeType\": 4}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc99\">Solution:</span> \n",
       "```python\n",
       "return (ketchup and not mustard) or (mustard and not ketchup)\n",
       "```"
      ],
      "text/plain": [
       "Solution: \n",
       "```python\n",
       "return (ketchup and not mustard) or (mustard and not ketchup)\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "q5.c.hint()\n",
    "q5.c.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc68646a",
   "metadata": {
    "papermill": {
     "duration": 0.009332,
     "end_time": "2025-03-16T22:20:12.007633",
     "exception": false,
     "start_time": "2025-03-16T22:20:11.998301",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 6. <span title=\"A bit spicy\" style=\"color: darkgreen \">🌶️</span>\n",
    "\n",
    "We’ve seen that calling `bool()` on an integer returns `False` if it’s equal to 0 and `True` otherwise. What happens if we call `int()` on a bool? Try it out in the notebook cell below.\n",
    "\n",
    "Can you take advantage of this to write a succinct function that corresponds to the English sentence \"does the customer want exactly one topping?\"?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "33cc4f3f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:12.028210Z",
     "iopub.status.busy": "2025-03-16T22:20:12.027833Z",
     "iopub.status.idle": "2025-03-16T22:20:12.035983Z",
     "shell.execute_reply": "2025-03-16T22:20:12.034997Z"
    },
    "papermill": {
     "duration": 0.020192,
     "end_time": "2025-03-16T22:20:12.037606",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.017414",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "parent.postMessage({\"jupyterEvent\": \"custom.exercise_interaction\", \"data\": {\"outcomeType\": 1, \"valueTowardsCompletion\": 0.2, \"interactionType\": 1, \"questionType\": 2, \"questionId\": \"6_OneTopping\", \"learnToolsVersion\": \"0.3.4\", \"failureMessage\": \"\", \"exceptionClass\": \"\", \"trace\": \"\"}}, \"*\")"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/markdown": [
       "<span style=\"color:#33cc33\">Correct:</span> \n",
       "\n",
       "This condition would be pretty complicated to express using just `and`, `or` and `not`, but using boolean-to-integer conversion gives us this short solution:\n",
       "```python\n",
       "return (int(ketchup) + int(mustard) + int(onion)) == 1\n",
       "```\n",
       "\n",
       "Fun fact: we don't technically need to call `int` on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...\n",
       "\n",
       "```python\n",
       "return (ketchup + mustard + onion) == 1\n",
       "```"
      ],
      "text/plain": [
       "Correct: \n",
       "\n",
       "This condition would be pretty complicated to express using just `and`, `or` and `not`, but using boolean-to-integer conversion gives us this short solution:\n",
       "```python\n",
       "return (int(ketchup) + int(mustard) + int(onion)) == 1\n",
       "```\n",
       "\n",
       "Fun fact: we don't technically need to call `int` on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...\n",
       "\n",
       "```python\n",
       "return (ketchup + mustard + onion) == 1\n",
       "```"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "def exactly_one_topping(ketchup, mustard, onion):\n",
    "    \"\"\"Return whether the customer wants exactly one of the three available toppings\n",
    "    on their hot dog.\n",
    "    \"\"\"\n",
    "    pass\n",
    "    return (int(ketchup)+int(mustard)+int(onion) == 1)\n",
    "\n",
    "# Check your answer\n",
    "q6.check()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d9ea45dd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:12.059057Z",
     "iopub.status.busy": "2025-03-16T22:20:12.058730Z",
     "iopub.status.idle": "2025-03-16T22:20:12.063317Z",
     "shell.execute_reply": "2025-03-16T22:20:12.061933Z"
    },
    "papermill": {
     "duration": 0.017239,
     "end_time": "2025-03-16T22:20:12.065234",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.047995",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#q6.hint()\n",
    "#q6.solution()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17ec3ed0",
   "metadata": {
    "papermill": {
     "duration": 0.009909,
     "end_time": "2025-03-16T22:20:12.085277",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.075368",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 7. <span title=\"A bit spicy\" style=\"color: darkgreen \">🌶️</span> (Optional)\n",
    "\n",
    "In this problem we'll be working with a simplified version of [blackjack](https://en.wikipedia.org/wiki/Blackjack) (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:\n",
    "\n",
    "- The player is dealt two face-up cards. The dealer is dealt one face-up card.\n",
    "- The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.\n",
    "- The dealer then deals additional cards to himself until either:\n",
    "    - the sum of the dealer's cards exceeds 21, in which case the player wins the round\n",
    "    - the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).\n",
    "    \n",
    "When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's \"total\" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)\n",
    "\n",
    "For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "568d8f44",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:12.106555Z",
     "iopub.status.busy": "2025-03-16T22:20:12.106205Z",
     "iopub.status.idle": "2025-03-16T22:20:12.110587Z",
     "shell.execute_reply": "2025-03-16T22:20:12.109622Z"
    },
    "papermill": {
     "duration": 0.017218,
     "end_time": "2025-03-16T22:20:12.112419",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.095201",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):\n",
    "    \"\"\"Return True if the player should hit (request another card) given the current game\n",
    "    state, or False if the player should stay.\n",
    "    When calculating a hand's total value, we count aces as \"high\" (with value 11) if doing so\n",
    "    doesn't bring the total above 21, otherwise we count them as low (with value 1). \n",
    "    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,\n",
    "    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.\n",
    "    \"\"\"\n",
    "    return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12b8a942",
   "metadata": {
    "papermill": {
     "duration": 0.009749,
     "end_time": "2025-03-16T22:20:12.132312",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.122563",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "This very conservative agent *always* sticks with the hand of two cards that they're dealt.\n",
    "\n",
    "We'll be simulating games between your player agent and our own dealer agent by calling your function.\n",
    "\n",
    "Try running the function below to see an example of a simulated game:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c82d3e4e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:12.153540Z",
     "iopub.status.busy": "2025-03-16T22:20:12.153213Z",
     "iopub.status.idle": "2025-03-16T22:20:12.159372Z",
     "shell.execute_reply": "2025-03-16T22:20:12.158262Z"
    },
    "papermill": {
     "duration": 0.019102,
     "end_time": "2025-03-16T22:20:12.161449",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.142347",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player starts with 10 and A (total = 21)\n",
      "Dealer starts with K\n",
      "\n",
      "__Player's turn__\n",
      "Player stays\n",
      "\n",
      "__Dealer's turn__\n",
      "Dealer hits and receives Q. (total = 20)\n",
      "Dealer stands.\n",
      "Player wins. 21 > 20\n"
     ]
    }
   ],
   "source": [
    "q7.simulate_one_game()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c35ab806",
   "metadata": {
    "papermill": {
     "duration": 0.009684,
     "end_time": "2025-03-16T22:20:12.181413",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.171729",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "The real test of your agent's mettle is their average win rate over many games. Try calling the function below to simulate 50000 games of blackjack (it may take a couple seconds):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9e31c516",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:12.202957Z",
     "iopub.status.busy": "2025-03-16T22:20:12.202550Z",
     "iopub.status.idle": "2025-03-16T22:20:13.284942Z",
     "shell.execute_reply": "2025-03-16T22:20:13.283600Z"
    },
    "papermill": {
     "duration": 1.095082,
     "end_time": "2025-03-16T22:20:13.286689",
     "exception": false,
     "start_time": "2025-03-16T22:20:12.191607",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player won 19047 out of 50000 games (win rate = 38.1%)\n"
     ]
    }
   ],
   "source": [
    "q7.simulate(n_games=50000)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59b51999",
   "metadata": {
    "papermill": {
     "duration": 0.010056,
     "end_time": "2025-03-16T22:20:13.307479",
     "exception": false,
     "start_time": "2025-03-16T22:20:13.297423",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Our dumb agent that completely ignores the game state still manages to win shockingly often!\n",
    "\n",
    "Try adding some more smarts to the `should_hit` function and see how it affects the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "cce5b602",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-16T22:20:13.328889Z",
     "iopub.status.busy": "2025-03-16T22:20:13.328544Z",
     "iopub.status.idle": "2025-03-16T22:20:14.412554Z",
     "shell.execute_reply": "2025-03-16T22:20:14.411371Z"
    },
    "papermill": {
     "duration": 1.097052,
     "end_time": "2025-03-16T22:20:14.414599",
     "exception": false,
     "start_time": "2025-03-16T22:20:13.317547",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player won 19059 out of 50000 games (win rate = 38.1%)\n"
     ]
    }
   ],
   "source": [
    "def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):\n",
    "    \"\"\"Return True if the player should hit (request another card) given the current game\n",
    "    state, or False if the player should stay.\n",
    "    When calculating a hand's total value, we count aces as \"high\" (with value 11) if doing so\n",
    "    doesn't bring the total above 21, otherwise we count them as low (with value 1). \n",
    "    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,\n",
    "    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.\n",
    "    \"\"\"\n",
    "    return False\n",
    "\n",
    "q7.simulate(n_games=50000)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92c44581",
   "metadata": {
    "papermill": {
     "duration": 0.010055,
     "end_time": "2025-03-16T22:20:14.435726",
     "exception": false,
     "start_time": "2025-03-16T22:20:14.425671",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Keep Going\n",
    "\n",
    "Learn about **[lists and tuples](https://www.kaggle.com/colinmorris/lists)** to handle multiple items of data in a systematic way."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fda10789",
   "metadata": {
    "papermill": {
     "duration": 0.009942,
     "end_time": "2025-03-16T22:20:14.456044",
     "exception": false,
     "start_time": "2025-03-16T22:20:14.446102",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "---\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/python/discussion) to chat with other learners.*"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [],
   "isGpuEnabled": false,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook"
  },
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
   "version": "3.10.12"
  },
  "learntools_metadata": {
   "lesson_index": 2,
   "type": "exercise"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 7.952845,
   "end_time": "2025-03-16T22:20:15.087504",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-03-16T22:20:07.134659",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
