import { useEffect, useReducer, useState } from "react"
import { LabelForm } from "./components/labelForm"
import { Message } from "./components/message"
import axios  from "axios";
import { Bars } from "react-loader-spinner";
import { Navigate } from "react-router-dom";
import Popup from "./components/popUp";



export default function Home() {



  const useAxios = (url, initialValue) => {
  const [data, setData] = useState(initialValue);
  const [loading, setLoading] = useState(true);


  useEffect(() => {
    const fetchData = async function () {
      try {
        setLoading(true);
        const response = await axios.get(url);
        if (response.status === 200) {
          setData(response.data);
        }
      } catch (error) {
        throw error;
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [url]);
  return { loading, messages: data };
};

  const [page, setPage] = useState(0);

  const [isOpen, setIsOpen] = useState(false);

  const togglePopup = () => {
    setIsOpen(!isOpen);
  }






  //console.log("|" + process.env.REACT_APP_API_END_POINT + "posts")

  const { loading, messages } = useAxios(
    process.env.REACT_APP_API_END_POINT + "posts"
  );




  //messages = messages.map( m => ({...m, counter: 0}));

  const formReducer = (state, event) => {
    const ide = messages[page]._id 
 
   
    return {[ide]: {...state[ide], [event.name] : event.value}}
  }



  const [formData, setFormDataH] = useReducer(formReducer, {});


  const handleChange = event => {
    const isCheckbox = event.target.type === 'checkbox';


    //console.log(event.target)

    if (isCheckbox) {
     
    }

    setFormDataH({
      name: event.target.name,
      value: isCheckbox?  event.target.checked : event.target.value,
    });

  }

  const handleSubmit = event => {
    event.preventDefault();

    //console.log("here", messages[page])


    //console.log("formdata", formData)
    messages[page].submited = true
    //console.log(messages)

    const to_check = [
       'network-support',
        'emotional-support',
        'informational-support',
        'esteem-support',
        'agreement' ,
        'disagreement',
        'gratitude',
        'congratulations',
        'sharing-experiences',
        'seeking-support' ,
        'emotional-polarity'
    ];

    
    let obj = {}

    let counter = 0;
    for (const key in  formData) {
      obj = {_id : key, labels: []}
      
      //console.log(formData[key])
      for (const key2 in formData[key]) {
        if (key2 !== 'emotion' && formData[key][key2] === 'positive') {
          obj['labels'].push(key2)
        }
        else if (key2 === 'emotion') {
          obj['labels'].push(formData[key][key2])
        }
        counter++;
      }
    }


    if (counter !== to_check.length) {
      togglePopup()
      return;
    }

   
    axios.put(process.env.REACT_APP_API_END_POINT + 'posts', {
      ...obj
    }).then(res => {
      //setArrowState(false);
      setPage(page + 1);
      //console.log('form gone well')
    })
    
    
    


  }

 

  if (loading) {
    return <div className="h-screen flex justify-center items-center">
      <Bars color="#8C2D19" height={80} width={80} />
      </div>
  }

  // after loading
  if (page === messages.length) {
   return <Navigate to='/thanks-menu'/>
  }


  return (

        <div className= "grid grid-cols-7 grid-flow-row ml-3">   

        {isOpen && <Popup
              content={<>
              <h1 className="m-5 text-center text-lg">Please select an options in all dropdowns</h1>
                  </>}
              handleClose={togglePopup}
            />}

            <div className="flex pt-3">
                
                <div className="px-3 text-black">
                {page + 1}/{messages.length}

                </div>
            </div>

            
            <>
                <div className="col-start-1 col-end-5 col-span-4 content-center h-[45rem] overflow-y-auto">
                    <Message key={messages[page]._id} text={messages[page].text}/>
                </div>

                <div className="col-start-5 col-span-3 px-4 h-[45rem] overflow-y-auto rounded py-3">
                    <form onSubmit={handleSubmit}> 
                   <LabelForm className="overflow-y-auto" key={messages[page]._id + '1'} setFormData={handleChange}/>
                    
                        <div className="p-5 pt-0 flex justify-end">
                           
                        <button  className="bg-slate-500 text-white p-2 rounded-md " type="submit">
                            Submit
                        </button> 
                        </div>
                    
                    </form>
                
                </div>
            </>
      


            
     

        </div>

  )


}