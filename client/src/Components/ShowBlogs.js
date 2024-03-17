import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const ShowBlogs = () => {
  const [blog, setBlog] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchBlog = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/blogs/${id}/`
        );
        setBlog(response.data);
      } catch (error) {
        console.error("Error fetching blog:", error);
      }
    };

    fetchBlog();
  }, [id]);

  return (
    <div className="container mt-5">
      {blog ? (
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">{blog.title}</h5>
            <p className="card-text p-4">{blog.content}</p>
          </div>
          <div className="card-footer">
            <small className="text-muted">
              Category: {blog?.category?.name} | Writer: {blog?.user}
            </small>
          </div>
        </div>
      ) : (
        <p>Blog yükleniyor...</p>
      )}
    </div>
  );
};

export default ShowBlogs;
