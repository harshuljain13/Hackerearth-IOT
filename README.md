# Hackerearth-IOT-hackathon

##Project Title: HALC- Health and Lifestyle companion

why This project? 
	This journey started around a year back when my father experienced a minor heart attack due to artery blockag. He is a fit
guy who wears the fitbit in order to take care of his health. But when he experienced the heart attack, we were unable to 
recognise it and got to know 3 days after the visiting the doctor. This all happened because we relied on a device that is 
a lifestyle device and not a clinical device. Hence, facing that critical time, i realised to build something that is more 
fruitful than fitbit.

## Tech Stack
```
1. Hardware
2. Python
3. Machine learning
4. Numpy
5. matplotlib
6. Thinkdsp
7. Django
8. Django rest framework
```

### A. Hardware preparation

### B. Python based Algorithms and Machine learning that supported the hardware:
```
1. get heart rate from the raw ppg signal using DSP in python- done [99% accurate]
2. get respiration rate from the raw ppg signal using DSP in python- done [98% accurate, fitbit does not give respiration rate]
3. get SPO2 from the raw ppg signal using DSP in python - done [95% accurate]
4. predictive BP calculation based on Random forest supervised classification in python - done [80% correct, need more training data]
5. Haemoglobin calculation suing formulas- not completed, but near
6. all ML part stays in real-everybit-new folder in github repository
```

### C. [Quick view of web app hosted on Heroku](https://dry-brushlands-94162.herokuapp.com)
```
https://dry-brushlands-94162.herokuapp.com

userid: hjain20
password: 12345
```

### D. How to Deploy server locally
```
git clone https://github.com/harshul1610/Hackerearth-IOT.git
cd Hackerearth-IOT
pip install -r requirements.txt
pip install -r requirements2.txt
./manage.py runserver 0.0.0.0:8000
```

### E. Video Link
[video1](https://www.youtube.com/watch?v=wczPOhFFhu8)
