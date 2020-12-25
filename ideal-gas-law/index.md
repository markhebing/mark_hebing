<html>
    <body>
        <p>The Ideal Gas Law states that pressure * volume  = moles * constant * temperature.</p>
        <p>Therefore, if moles and temperature remain the same, it stands to reason that if either pressure or volume change, then the change in the accompanying value can be calculated.</p>
        <p>P1 * V1 = P2 * V2</p>
        <p>Enter three of the values below to calculate the fourth:</p>
        <form onsubmit="return calculate_missing_variable();">
            <label for="p1">Enter pressure 1:</label>
            <input type="text" id="p1"><br/>
            <label for="v1">Enter volume 1:</label>
            <input type="text" id="v1"><br/>
            <label for="p2">Enter pressure 2:</label>
            <input type="text" id="p2"><br/>
            <label for="v2">Enter volume 2:</label>
            <input type="text" id="v2"><br/><br/>
            <button>Submit</button>
         </form>
         <script>
             function calculate_missing_variable(p1, v1, p2, v2)
             {
                var p1=document.getElementById("p1").value;
                var v1=document.getElementById("v1").value;
                var p2=document.getElementById("p2").value;
                var v2=document.getElementById("v2").value;
                if (p1 == "" && v1 != "" && p2 != "" && v2 != "")
                {
                    p1 = p2 * v2 / v1;
                    document.write("Pressure 1 = " + p1 + "<br/><br/>");
                    document.write("Reload page to perform another calculation.");
                }
                else if (v1 == "" && p1 != "" && p2 != "" && v2 != "")
                {
                    v1 = p2 * v2 / p1;
                    document.write("Volume 1 = " + v1+ "<br/><br/>");
                    document.write("Reload page to perform another calculation.");
                }
                else if (p2 == "" && v2 != "" && p1 != "" && v1 != "")
                {
                    p2 = p1 * v1 / v2;
                    document.write("Pressure 2 = " + p2+ "<br/><br/>");
                    document.write("Reload page to perform another calculation.");
                }
                else if (v2 == "" && p2 != "" && p1 != "" && v1 != "")
                {
                    v2 = p1 * v1 / p2;
                    document.write("Volume 2 = " + v2+ "<br/><br/>");
                    document.write("Reload page to perform another calculation.");
                }
                else
                {
                    document.write("Missing values. Reload page and input three out of the four values to perform calculation.");
                }
            }
         </script>
    </body>
</html>
