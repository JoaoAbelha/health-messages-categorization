import React, { useState } from 'react';
import Popup from './popUp';
import { schema } from '../schema';

export function LabelForm(props) {


    const possible_binary_inputs = [
        'network-support', 'emotional-support', 'informational-support', 'esteem-support', 'agreement', 'disagreement',
        'gratitude', 'congratulations', 'sharing-experiences', 'seeking-support'
    ];

    const mappings = {
        'network-support': schema.filter((element) => element.title ===  'Network Support')[0],
        'emotional-support': schema.filter((element) => element.title ===  'Emotional Support')[0] ,
        'informational-support':  schema.filter((element) => element.title ===  'Informational Support')[0],
        'esteem-support': schema.filter((element) => element.title ===  'Esteem Support')[0],
        'agreement':  schema.filter((element) => element.title === 'Agreement')[0] ,
        'disagreement': schema.filter((element) => element.title === 'Disagreement')[0],
        'gratitude': schema.filter((element) => element.title === 'Gratitude')[0],
        'congratulations': schema.filter((element) => element.title === 'Congratulations')[0],
        'sharing-experiences' : schema.filter((element) => element.title === 'Sharing Experiences')[0],
        'seeking-support' : schema.filter((element) => element.title === 'Seeking Support')[0],
        'emotional-polarity': schema.filter((element) => element.title === 'Emotional Polarity')[0]
    }

    //console.log(mappings)

    const [isOpen, setIsOpen] = useState(false);

    const [popUpsState, setPopUpsState] = useState([false, false, false, false, false, false, false, false, false, false]);


    const handlePopUp = (index) => {
        setPopUpsState(prevState => prevState.map((item, idx) => idx === index ? !item : item))
    };

 
    const togglePopup = () => {
      setIsOpen(!isOpen);
    }

    return (
        <div>
            <fieldset id = "input-wrapper-1" className="my-4 mx-2"> 

        <div className='flex gap-2'>
            
            <legend className="d-none">What are the emotional polarity present in the text? </legend>

            <div>
                <input
                type="button"
                title="help"
                value="?"
                className='cursor-pointer rounded-lg bg-[#8C2D19] text-white px-2'
                onClick={togglePopup}
                />
                    {isOpen && <Popup
                    content={<>
                    <h1 className='text-center mb-3 font-bold'>{mappings['emotional-polarity'].title}</h1>
                    <p>
                        {mappings['emotional-polarity'].description}

                    </p>
                    <p className='font-light mt-2 text-gray-500 text-sm'>
                      <strong>Example: </strong>{mappings['emotional-polarity'].example}
                    </p>
                    {mappings['emotional-polarity'].example2 !== undefined && <p className='font-light mt-2 text-gray-500 text-sm'>
                      <strong>Example: </strong>{mappings['emotional-polarity'].example2}
                    </p>}

                         </>}
                    handleClose={togglePopup}
                    />}
            </div>
        </div>

            <div className= "flex justify-around content-center my-3">


                <div className="grid grid-cols-2 gap-2 content-end ">
                    <label htmlFor="negative">Negative</label>
                    <input required onChange={props.setFormData} className="self-center" type="radio" name="emotion" value="negative" id="negative"/>
                </div>

                <div className="grid grid-cols-2 gap-2 content-end ">
                    <label htmlFor="neutral">Neutral</label>
                    <input required onChange={props.setFormData} className="self-center" id = "neutral" type="radio" name="emotion" value="neutral"/>
                </div>

                <div className="grid grid-cols-2 gap-2 content-end ">
                    <label htmlFor="positive">Positive</label>
                    <input required onChange={props.setFormData} className="self-center" type="radio" name="emotion" value="positive" id="positive"/>
                </div>
            </div>

        </fieldset>

        {possible_binary_inputs.map((field, idx) => <fieldset key={field} className="my-6">
            <div className="flex justify-between mr-5">
               
                <div className='flex gap-2'>
            
                    <legend>Does the text depict {field.replace('-', ' ')} ? </legend>

                    <div>
                        <input
                        type="button"
                        title="help"
                        value="?"
                        className='cursor-pointer rounded-lg bg-[#8C2D19] text-white px-2'
                        onClick={() => handlePopUp(idx)}
                        />
                            {popUpsState[idx] && <Popup
                            content={<>
                            <h1 className='text-center mb-3 font-bold'>{mappings[field].title}</h1>
                            <p>
                                {mappings[field].description}

                            </p>
                            <p className='font-light mt-2 text-gray-500 text-sm'>
                            <strong>Example: </strong>{mappings[field].example}
                            </p>
                            {mappings[field].example2 !== undefined && <p className='font-light mt-2 text-gray-500 text-sm'>
                            <strong>Example: </strong>{mappings[field].example2}
                            </p>}

                                </>}
                            handleClose={() => handlePopUp(idx)}
                            />}
                    </div>
                </div>
                
                    <select defaultValue={"hidden"} onChange={props.setFormData} name={`${field}`} id={`${field}`}>
                        <option value= "hidden" hidden disabled > -- select an option -- </option>
                        <option value="positive">Yes</option>
                        <option value="negative">No</option>
                    </select>
            </div>



        </fieldset>)}

      </div>



    );
}