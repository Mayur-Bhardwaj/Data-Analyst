{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bf4f1dc7-77f1-4f43-bb89-09af83aac212",
   "metadata": {},
   "source": [
    "# Print Pattern\n",
    "# 1\n",
    "# 1 2 1 \n",
    "# 1 2 3 2 1 \n",
    "# 1 2 3 4 3 2 1\n",
    "# 1 2 3 4 5 4 3 2 1 \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "25ced7fd-a9b3-4bc7-af72-3790c9fa01bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#  Here 3 loops used:\n",
    "# 1. Loop_1 is used for control no of lines.\n",
    "# 2. Loop_2 is used for increment numbers. \n",
    "# 3. Loop_3 is used for decrement numbers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b0c73c73-de59-49db-9044-f7b2a98e16aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "1 2 1 \n",
      "1 2 3 2 1 \n",
      "1 2 3 4 3 2 1 \n",
      "1 2 3 4 5 4 3 2 1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):  # for controlling the number of lines \n",
    "    for j in range(1, i+1):  # for increment numbers\n",
    "        print(j, end=\" \")\n",
    "    for k in range(i-1, 0, -1):   # for decrement numbers.abs\n",
    "        print(k, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "924431b4-a5ce-4677-be72-4a5b23844937",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
