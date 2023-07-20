import React, {useState, useEffect } from 'react';

function HatsForm( ) {
    const [locations, setLocations] = useState([]);

    const [fabric, setFabric] = useState('')
    const handleFabricChange = (event) => {
        const value = event.target.value;
        setFabric(value);
    }
    const [styleName, setStyleName] = useState('')
    const handleStyleNameChange = (event) => {
        const value = event.target.value;
        setStyleName(value);
    }
    const [color, setColor] = useState('')
    const handleColorChange = (event) => {
        const value = event.target.value;
        setColor(value);
    }
    const [picture, setPicture] = useState('')
    const handlePictureChange = (event) => {
        const value = event.target.value;
        setPicture(value);
    }
    const [location, setLocation] = useState('')
    const handleLocationChange = (event) =>{
        const value = event.target.value;
        console.log(event.target)
        setLocation(value);
    }
    const fetchData = async () => {
      const url = 'http://localhost:8100/api/locations/';
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setLocations(data.locations)
        console.log(data)
      }
    }

    useEffect(() => {
        fetchData();
    }, []);
    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {};
        data.fabric = fabric;
        data.style_name = styleName;
        data.color = color;
        data.picture = picture;
        data.location = location;
        console.log(data);
        const hatUrl = 'http://localhost:8090/api/hats/';
        const fetchConfig = {
        method: "post",
        body: JSON.stringify(data),
        headers: {
        'Content-Type': 'application/json',
        },
    };
    const response = await fetch(hatUrl, fetchConfig);
    if (response.ok) {
        const newHat = await response.json();
        console.log(newHat);
        setFabric('');
        setColor('');
        setPicture('');
        setStyleName('');
    } else if (!response.ok) {
        console.log(fetchConfig)
        console.log(location)
    }
    }
    return (
        <>
        <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Create a new hat</h1>
            <form onSubmit= {handleSubmit} id="create-hat-form">
              <div className="form-floating mb-3">
                <input onChange= {handleFabricChange} placeholder="Fabric" required type="text" name="fabric" id="fabric" className="form-control" value={fabric} />
                <label htmlFor="fabric">Fabric</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange= {handleStyleNameChange} placeholder="Style Name" required type="text" name="style_name" id="style_name" className="form-control" value={styleName}/>
                <label htmlFor="style_name">Style</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange= {handleColorChange} placeholder="Color" required type="text" name= "color" id="color" className="form-control" value={color}/>
                <label htmlFor="color">Color</label>
              </div>
              <div className="form-floating mb-3">
                <input onChange= {handlePictureChange} placeholder="Picture url" required type="url" name= "picture" id="picture" className="form-control" value={picture}/>
                <label htmlFor="picture">Picture URL</label>
              </div>
              <div className="mb-3">
                <select onChange= {handleLocationChange} required id="location" name= "location" className="form-select" value={location}>
                  <option value="">Choose a location</option>
                  {locations.map(location => {
                    return (
                        <option key={location.id} value={location.href}>
                            {location.closet_name}
                        </option>
                    );
                  })}
                </select>
              </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
      </>
    );
}

export default HatsForm;
