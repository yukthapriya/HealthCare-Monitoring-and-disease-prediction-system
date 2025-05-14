# Public Healthcare Monitoring and Disease Prediction System

## Overview

This project report describes a system for Public Healthcare Monitoring and Disease Prediction.  The system uses machine learning techniques to predict the likelihood of diseases, specifically diabetes, in patients.  It takes patient symptoms as input and provides a disease prediction, along with a recommended diet plan.

## Purpose

The project aims to:

* Develop a system that predicts diseases (with a focus on diabetes) based on patient-provided symptoms.
* Recommend appropriate diet plans to patients based on the predictions.
* Examine the use of machine learning techniques in healthcare recommender systems.
* Provide a resource for new researchers in this area.

## Features

* Disease prediction based on patient symptoms.
* Diet plan recommendations.
* Uses machine learning (Random Forest) for feature selection and disease prediction.
* Analysis of machine learning techniques in health recommender systems.

## Tech Stack

* Python
* Django
* Spyder
* SQLite

## System Architecture

The system architecture includes the following modules:

* User Module: Handles user registration, authentication, profiles, and input of health metrics.
* Database Module:  Stores user profiles, health metrics, and prediction results using SQLite.
* Training Module: Trains the machine learning model (Random Forest) on the data.
* Disease Prediction Module: Predicts the likelihood of disease based on input symptoms.
* Recommendation Module:  Recommends a diet plan.

The system follows a web-based architecture.

## Installation

1.  Set up the required hardware and software (see "Hardware & Software Requirements" in the full report).
2.  Install the necessary Python packages (Django, etc.).
3.  Configure the SQLite database.
4.  Deploy the web application.

## Usage

1.  Users register and log in to the system.
2.  Users input their symptoms and health metrics.
3.  The system predicts the likelihood of disease.
4.  The system provides a recommended diet plan.

## Future Work

The report suggests the following future enhancements:

* Add a user panel.
* Add an admin panel.
* Implement login authentication.
* Add images and rating functionality for products.

## Contributions

* M.YUKTHA PRIYA 
* M.RAMYA 
* P.VARSHINI 
* P.NYMISHA KEZIA 

## Acknowledgements

* Mrs.K.R.LAVANYA, M.Tech., Assistant Professor (Adhoc), Department of CSE.
* Dr. B.LALITHA, M.Tech., Ph.D., Associate Professor & Head of the Department, Department of CSE.
* Jawaharlal Nehru Technological University Anantapur College of Engineering, Kalikiri.
