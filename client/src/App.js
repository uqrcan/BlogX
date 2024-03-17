import React from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useNavigate,
} from "react-router-dom";
import Blogs from "./Components/Blog";
import ShowBlog from "./Components/ShowBlogs";
import Login from "./Components/pages/Login";
import Register from "./Components/pages/Register";
import Navbar from "./Components/Navbar";
function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>

      <div>
        <div className="column-100">
          <Routes>
            <Route path="/" element={<Blogs />} />
            <Route path="/blog/:id" element={<ShowBlog />} />
          </Routes>
          <footer>
            <div className="container">
              <div className="row">
                <div className="col-md-12">
                  <div className="footer-copyright text-center py-3">
                    © 2024 Copyright:
                    <a href="">BlogX</a>
                  </div>
                </div>
              </div>
            </div>
          </footer>
        </div>
      </div>
    </Router>
  );
}

export default App;
