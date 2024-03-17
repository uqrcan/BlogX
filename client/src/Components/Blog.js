import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Row, Col } from "react-bootstrap";
import BlogCard from "./BlogCard";

const Blogs = () => {
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/blogs/");
        setBlogs(response.data);
      } catch (error) {
        console.error("Error fetching blogs:", error);
      }
    };
    fetchBlogs();
  }, []);

  return (
    <Container>
      <h1 className="my-4">Bloglar</h1>
      <Row xs={1} md={2} lg={3} className="g-4">
        {blogs.map((blog) => (
          <Col key={blog.id}>
            <BlogCard
              title={blog.title}
              content={blog.content}
              blogId={blog.id}
            />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Blogs;
