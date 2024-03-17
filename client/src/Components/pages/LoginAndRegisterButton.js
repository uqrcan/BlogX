import React from "react";
import { Link } from "react-router-dom";

const LoginAndRegisterButton = () => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div style={{ display: "flex", flexDirection: "row" }}>
        <Link to="/login" style={{ margin: "0 10px" }}>
          <button className="btn btn-primary m-2">Login</button>
        </Link>
        <Link to="/register" style={{ margin: "0 10px" }}>
          <button className="btn btn-primary m-2">Register</button>
        </Link>
      </div>
    </div>
  );
};

export default LoginAndRegisterButton;
