import "./App.css";
import DescriptionContainter from "./components/DescriptionContainter";
import ImageContainer from "./components/ImageContainer";
import { Navbar } from "./components/Navbar";
function App() {
  return (
    <div className="main_container">
      <div className="mynav">
        <Navbar />
      </div>

      <div className="product_container ">
        <div className="row p-0">
          <div className="col-lg-7 padding_right50px">
            <ImageContainer />
          </div>
          <div class="col-lg-5 p-0 pl-4">
            <DescriptionContainter />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
