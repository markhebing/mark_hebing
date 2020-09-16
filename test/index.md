<html>
    <body>
        <script>
            function add_up(number)
            {
                counter = 1;
                number_sum = 0;
                while (counter <= number)
                {
                    number_sum = number_sum + counter;
                    document.write(number_sum + "</br>");
                    counter = counter + 1;
                }
                return number_sum;
            }
        </script>
        <script>
            document.write(add_up(10000) + "</br>");
        </script>
    </body>
</html>
