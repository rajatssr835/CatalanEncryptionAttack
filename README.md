# CatalanEncryptionAttack

1) datasetgen.py ---> This file generates random plaintexts and using the rule encode in line 53 (i.e Catalan Key) corresponding ciphertext is generated. Currently the code generates 1000 plaintext and ciphertext pairs

2) MLCode.py -----> This is the machine learning model developed using Scikit-learn

3) dataset.csv  -----> this is the dataset containing plaintext, ciphertext pairs. The first 16 columns of a row are 16-bits of plaintext while next 16 columns are ciphertext bits. Currently the dataset contains 1000 plaintext ciphertext pairs.
