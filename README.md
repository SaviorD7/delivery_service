**START UP**:

``docker-compose up --build ``

**Info**:

1. Use your credentials file from GC and put it into root directory 
2. Endpoint  `/upload_data` download data from GS. You can change ID of GS in  `utils/data` to use your own GS with your own credentials.
2. Endpoint  `/update_data` update data from GS, include deleting, editing data.


**Possible improvements**
1. Add Front-end part to interaction with service
2. Write more verifications for bad data