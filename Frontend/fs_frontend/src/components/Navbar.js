import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import logo from "../img/logo.png";

export const Navbar = () => {
  return (
    <Router>
      <div>
        <nav className="navbar navbar-expand-lg bg-transparent">
          <div className="container-fluid">
            <Link className="navbar-brand" to="#">
              <img className="logo" src={logo} alt="" />
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNavAltMarkup"
              aria-controls="navbarNavAltMarkup"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div className="navbar-nav ms-auto">
                <Link className="nav-link  nav_item_custom" aria-current="page" to="#">
                  Home
                </Link>
                <Link className="nav-link nav_item_custom fs_active" to="#">
                  Products
                </Link>
                <Link className="nav-link nav_item_custom" to="#">
                  Blog
                </Link>

                <Link className="nav-link nav_item_custom" to="#">
                  Contact US
                </Link>

                <button className=" btn_fs btn_login">Login</button>
                <button className=" btn_fs btn_signup">Sign Up</button>
                
              </div>
            </div>
          </div>
        </nav>
      </div>
    </Router>
  );
};
