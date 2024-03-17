import React from "react";
import { Link, useLocation } from "react-router-dom";

const Navbar = () => {
  const location = useLocation();

  // Kullanıcı adını localStorage'den al
  const userName = localStorage.getItem("userName");

  // Çıkış işlemi
  const handleLogout = () => {
    // Kullanıcı adını ve token'ı localStorage'den kaldır
    localStorage.removeItem("userName");
    localStorage.removeItem("token");

    // Sayfayı yenile
    window.location.reload();
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" to="/">
          BlogX
        </Link>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link
                className={`nav-link ${location.pathname === "/" && "active"}`}
                to="/"
              >
                Home
              </Link>
            </li>
          </ul>
          {userName ? (
            <div className="d-flex">
              <p className="nav-link me-3">{userName}</p>
              <button className="btn btn-outline-danger" onClick={handleLogout}>
                Logout
              </button>
            </div>
          ) : (
            <Link className="btn btn-primary" to="/login">
              Login
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

// import React from "react";
// import { NavLink } from "react-router-dom";
// import LoginAndRegisterButton from "./pages/LoginAndRegisterButton";

// const Navbar = () => {
//   return (
//     <nav className="navbar navbar-expand-lg navbar-light bg-light">
//       <div className="container-fluid">
//         <NavLink className="navbar-brand" to="/">
//           Blog Uygulaması
//         </NavLink>
//         <LoginAndRegisterButton />
//       </div>
//     </nav>
//   );
// };

// export default Navbar;
