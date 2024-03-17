import React from "react";
import { Card } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

const BlogCard = ({ title, content, blogId }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/blog/${blogId}`);
  };

  return (
    <Card style={{ width: "18rem", cursor: "pointer" }} onClick={handleClick}>
      <Card.Body>
        <Card.Title>{title}</Card.Title>
        <Card.Text>{content.slice(0, 90)}...</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default BlogCard;
