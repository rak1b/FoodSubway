import React from "react";
import img1 from "../img/img1.png";
import imgsm1 from "../img/imgsm1.png";
import imgsm2 from "../img/imgsm2.png";
import imgsm3 from "../img/imgsm3.png";

const ImageContainer = () => {
  return (
    <>
      <div className="row img1">
        <div className="col-12">
          <img src={img1} alt="" />
        </div>
      </div>
      <div className="row mt-4">
        <div className="col-4 imgsm1">
          <img src={imgsm1}  className="" alt="" />
        </div>
        <div className="col-4 imgsm2">
          <img src={imgsm2} className=""  alt="" />
        </div>
        <div className="col-4 imgsm3">
          <img src={imgsm3} className=""  alt="" />
        </div>
      </div>
    </>
  );
};

export default ImageContainer;
