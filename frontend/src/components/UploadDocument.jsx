import React, { useState } from "react";
import axios from "axios";

const UploadDocument = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file first.");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", file);
  
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",  // Explicitly setting the header
        },
      });
      setMessage(`Upload successful! ${response.data.message || ""}`);
    } catch (error) {
      console.error("Upload failed:", error);
      setMessage("Upload failed. Please try again.");
    }
  };
  

  return (
    <div>
      <h2>Upload Document</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default UploadDocument;

