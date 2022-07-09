import {
  Accordion,
  AccordionItem,
  AccordionItemHeading,
  AccordionItemButton,
  AccordionItemPanel,
} from 'react-accessible-accordion';
import { NavLink } from "react-router-dom";

import {schema} from './../src/schema';

import 'react-accessible-accordion/dist/fancy-example.css';

export default function Instructions() {
   


    return (
      <main className="h-full mb-4 mx-4">
        <div className="bg-white p-4 flex flex-col justify-center"> 

          <img className="m-0 ml-5 mb-7" height="auto" width={200} src={process.env.PUBLIC_URL + "logouporto.png"} alt="Uporto icon"/>
          <div className='flex'>
            <h2 className='py-5'> <strong>Before</strong> clicking on the participate tab, read the following carefully: </h2>
            <span className='m-0 ml-auto font-light text-gray-400'>4min-read</span>
          </div>

          <h3 className='font-bold my-4'>Context:</h3>
          <ul className='list-[upper-roman] mx-5'>
            <li className='my-1'>
            I am João Paulo Abelha, a student currently enrolled in Mestrado em Engenharia Informática e Computação doing its Master Thesis under the supervision of the Professor Carla Teixeira Lopes.            </li>
            <li>
              My Thesis' title is <span className='text-[#8C2D19] font-bold'>Automatic categorization of health-related messages in online health communities</span>, and the objective is to use machine learning to label messages without human intervention. For this purpose, we first need to build a labeled dataset.
            </li>
            <li>
            This website has the objective of people aiding me in labeling messages from health forums.
            </li>
            <li  className='my-1'>
            We extracted messages from real health forums. For this reason, they may contain sensitive content.
            </li>
            <li  className='my-1'>
            The messages to annotate are in English.
            </li>
            <li className='my-1'>
            On the 'Participate' Page, you will read and verify if specific characteristics are present in a message. After submitting a message, you can use an arrow in the top left part of the page to go to the following message.
          </li>
          <li className='my-1'>
          The amount of time needed for the average reader to complete the task takes somewhere from <strong>5 to 10 minutes</strong>
          </li>
          <li className='my-1'>
          In case you have some doubts during the classification, the schema below can always be consulted as it has a definition and examples(s).
          </li>
          <li  className='my-1'>
            If you have any doubts, you can contact me using the following email <span className="text-slate-700 hover:underline font-bold">healthforumlabeling@gmail.com
</span>
            </li>
          </ul>
 

          <h3 className='font-bold my-5'>Scheme:</h3>
          <Accordion allowMultipleExpanded={true} allowZeroExpanded={true}>
            {schema.map((field, index) => 
            <AccordionItem key={index}>
                <AccordionItemHeading>
                    <AccordionItemButton>
                        {field.title}
                    </AccordionItemButton>
                </AccordionItemHeading>
                <AccordionItemPanel>
                    <p>
                        {field.description}
                    </p>
                    <p className='font-light mt-2 text-gray-500 text-sm'>
                      <strong>Example: </strong>{field.example}
                    </p>
                   { field.example2 !== undefined && <p className='font-light mt-2 text-gray-500 text-sm'>
                      <strong>Example: </strong>{field.example2}
                    </p>}
                </AccordionItemPanel>

            </AccordionItem>)}
        </Accordion>
              

        <span className='flex justify-between my-10'>
        <span>Thanks for your colaboration!</span>
        <NavLink className="text-white mr-10 bg-slate-500 hover:bg-white hover:text-slate-500 border-2 border-slate-500 p-3 rounded-md" to='/participate'>Participate</NavLink>
          
        </span>
   
        </div>    
      </main>
    );
  }