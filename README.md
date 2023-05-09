# How to run the project ?

In order to run the project, you will need to install on your computer the following libraries:

```
mpyc
numpy
gmpy2
pandas
scikit-learn
```

You can install them by running:

```
pip install -r ./src/data_owner/requirements.txt
```

If you want to execute the project directly, you can use the following command inside the src folder:

```
python main.py --parties 3
```

This will execute the script and prompt you all the required information about your patient.
It will output both prediction by SMC computation and by the given function.


If you want to run it inside containers, you can use the following command:

```
docker-compose up
```