## Project 07: Static Web Hosting on S3

This project explores hosting a static website directly on Amazon S3, leveraging its scalability and cost-effectiveness for simple web pages.

**Objective:**

* Deploy a basic website using S3's static web hosting capability.
* Understand the process of configuring S3 buckets and website settings.
* Apply knowledge gained from existing tutorials and resources.

**Implementation:**

* Followed the comprehensive tutorial: [https://youtu.be/pReSVJcBeuA?si=Bf0O0vKUgazrWVa4](https://youtu.be/pReSVJcBeuA?si=Bf0O0vKUgazrWVa4)
* Configured an S3 bucket with appropriate permissions and website hosting settings.
* Uploaded static website files (HTML, CSS, JavaScript) to the S3 bucket.
* Defined custom domain mapping (optional) for a professional URL.

**Bucket Configuration:**

Here's the detailed S3 bucket configuration process:

1. **Create an S3 bucket:** Choose a unique and descriptive name for your website.
2. **Set Public Access Permissions:** In the "Permissions" tab, under "Public access settings", tick the checkbox for "Block all public access". This ensures only authorized users can access your website files.
3. **Enable Static Website Hosting:** In the "Properties" tab, under "Static website hosting", click "Edit". 
    * Select "Redirect requests to a different host" and enter the error document (e.g., "index.html") in the "Index document" field. 
    * Select "Redirect requests with other object keys to a different host" and enter the main document (e.g., "index.html") in the "Error document" field.
    * Click "Save".
4. **Set Public Read Permissions:** Under "Permissions" again, go to "Bucket Policy" and add a policy snippet granting public read access to objects within the bucket:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

Replace `YOUR_BUCKET_NAME` with your actual bucket name.
(https://github.com/zareefrj/Cloud_Projects/assets/76507749/4cfff3be-65cf-4e6f-820d-f91b72275d88)

5. **Upload Website Files:** Upload your static website files (HTML, CSS, JavaScript) to the root directory of your S3 bucket.
(https://github.com/zareefrj/Cloud_Projects/assets/76507749/1bb05c89-b287-470b-9fdb-dd55b9f9491a)
