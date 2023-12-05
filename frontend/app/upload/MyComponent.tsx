/* eslint-disable @typescript-eslint/no-unused-vars */
//import React, { useState } from 'react';
"use client";
import { AnimatePresence } from "framer-motion";
import React, { useCallback, useRef, useState } from 'react';
import { useTranslation } from "react-i18next";

import Button from "@/lib/components/ui/Button";
import Card from "@/lib/components/ui/Card";
import Field from "@/lib/components/ui/Field";
import { useBrainContext } from "@/lib/context/BrainProvider/hooks/useBrainContext";
import { useSupabase } from '@/lib/context/SupabaseProvider';
import { useToast } from '@/lib/hooks';
import { redirectToLogin } from '@/lib/router/redirectToLogin';
import { useEventTracking } from '@/services/analytics/useEventTracking';

// Define the props type
interface MyComponentProps {
  message: string; // Example prop: message of type string
}

const MyComponent = (props: MyComponentProps): JSX.Element => {
  //const { urlInputRef, isCrawling, crawlWebsite } = useCrawler();
  //const { dirInputRef, isIndexing, indexDirectory } = useState();
  //const { currentBrain } = useBrainContext();
  //const { t } = useTranslation(["translation", "upload"]);
  
  const [inputValue, setInputValue] = useState(''); // State for the input value

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    // Update the inputValue state when the input value changes
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
    // Handle button click here, e.g., display the input value
    alert(`You entered: ${inputValue}`);
  };

  return (
    <>
      <div className="w-full">
      <div className="flex justify-center gap-5 px-6">
        <div className="max-w-xl w-full">
          <div className="flex-col justify-center gap-5">
            <Card className="h-32 flex gap-5 justify-center items-center px-5">
              <div className="text-center max-w-sm w-full flex flex-col gap-5 items-center">
              <input
                type="text"
                value={inputValue}
                onChange={handleInputChange}
                placeholder="Enter text (Directory Path)..."
                />
                <Button onClick={handleButtonClick}>Index Feedback Loop</Button>
              </div>
            </Card>
            <Card className="h-32 flex gap-5 justify-center items-center px-5">
              <h1>{props.message}</h1>
              <input
                type="text"
                value={inputValue}
                onChange={handleInputChange}
                placeholder="Enter text..."
              />
              <Button onClick={handleButtonClick}>Convert</Button>
          </Card>
          </div>
        </div>
      </div>
    </div>
    </>
  );
};

export default MyComponent;
