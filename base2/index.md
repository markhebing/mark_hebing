<html>
    <body>
        <script>  
            function randomNumber(min, max)
            {  
                return Math.floor(Math.random() * (max - min) + min); 
            }  
            </script>  
        <script>
            function convert_base_2(number)
            {
                base_ten_array = [524288, 262100, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1];
                binary_number_array = [];
                counter = 0;
                while (counter < base_ten_array.length)
                {
                    if (number >= base_ten_array[counter])
                    {
                        binary_number_array[counter] = 1;
                        number = number - base_ten_array[counter];
                    }
                    else
                    {
                        binary_number_array[counter] = 0;
                    }
                    document.write(binary_number_array[counter]);
                    counter = counter + 1;
                }
            }
        </script>
        <script>
            convert_base_2(1); document.write("</br>");
            convert_base_2(2); document.write("</br>");
            convert_base_2(4); document.write("</br>");
            convert_base_2(8); document.write("</br>");
            convert_base_2(16); document.write("</br>");
            convert_base_2(32); document.write("</br>");
            convert_base_2(64); document.write("</br>");
            convert_base_2(128); document.write("</br>");
            convert_base_2(256); document.write("</br>");
            convert_base_2(512); document.write("</br>");
            convert_base_2(1024); document.write("</br>");
            convert_base_2(2048); document.write("</br>");
            convert_base_2(4096); document.write("</br>");
            convert_base_2(8192); document.write("</br>");
            convert_base_2(16384); document.write("</br>");
            convert_base_2(32768); document.write("</br>");
            convert_base_2(65536); document.write("</br>");
            convert_base_2(131072); document.write("</br>");
            convert_base_2(262100); document.write("</br>");
            convert_base_2(524288); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
            convert_base_2(randomNumber(1, 1000000)); document.write("</br>");
        </script>
    </body>
</html>
