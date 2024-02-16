## Project 08: AWS Valentine's Gift - Sending Personalized Wishes with Amplify and Lambda
(https://dev.dld3f38e1u8u.amplifyapp.com/)

This project brings the spirit of Valentine's Day to life by creating a web application on AWS Amplify that sends personalized messages to users.
* Followed this comprehensive tutorial for guidance: [https://youtu.be/7m_q1ldzw0U?si=3w_NuetKhB3j7rD8](https://youtu.be/7m_q1ldzw0U?si=3w_NuetKhB3j7rD8)
**Objective:**

* Design and deploy a user-friendly website on Amplify, prompting users to enter their names.
* Develop a Python Lambda function triggered by user submission, generating a custom Valentine's message.
* Configure an API Gateway endpoint to expose the Lambda function as a REST API.
* Seamlessly integrate the API call and message display within the Amplify website upon form submission.

**Implementation:**

* **Amplify Website:**
    * Hosted the website by submitting a zip file containing the HTML, CSS, Javascript files for the website.
    * Design an intuitive interface for name input and submission.
    * Integrate API Gateway endpoint for calling the Lambda function on submit.
      (https://github.com/zareefrj/Cloud_Projects/assets/76507749/1a3c2b4e-a98c-4ade-9f20-3d506c4a87e1)

* **Lambda Function (Python):**
    * Develop a Python function triggered by API Gateway requests.
    * Access the submitted name from the request payload.
    * Craft a personalized Valentine's message incorporating the user's name.
    * Return the generated message as the API response.
    (https://github.com/zareefrj/Cloud_Projects/assets/76507749/6d6b6c7a-73f9-487b-8845-8b316debd4cc)

* **API Gateway:**
    * Create a REST API resource and method corresponding to the Lambda function.
    * Configure appropriate security and authorization settings.
      (https://github.com/zareefrj/Cloud_Projects/assets/76507749/d776a96d-5fa1-45ae-920c-58b5ed784661)
