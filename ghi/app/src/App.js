import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatsList from './Hatslist';


function App(props) {
  if (props.hats === undefined){
    return null;
  }
  return (
      <>
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route index element={<MainPage />} />
          <Route path="hats">
            <Route index element={<HatsList hats={props.hats} />} />
            {/* <Route path="new" element={<HatForm />} /> */}
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
    </>
  );
}

export default App;
