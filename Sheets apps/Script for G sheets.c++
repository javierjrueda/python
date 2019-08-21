function endtask() {
  var spreadsheet = SpreadsheetApp.getActive();
  
  //Insertamos una fila nueva en AUX
  spreadsheet.getRange('G4').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('2:2').activate();
  spreadsheet.getActiveSheet().insertRowsBefore(spreadsheet.getActiveRange().getRow(), 1);
  spreadsheet.getActiveRange().offset(0, 0, 1, spreadsheet.getActiveRange().getNumColumns()).activate();
  
  // Copiamos nombre operario
  spreadsheet.getRange('B2').activate();
  spreadsheet.getRange('\'Time tracking\'!G4').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Copiamos material
  spreadsheet.getRange('C2').activate();
  spreadsheet.getRange('\'Time tracking\'!G7').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Copiamos proceso
  spreadsheet.getRange('D2').activate();
  spreadsheet.getRange('\'Time tracking\'!G10').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Copiamos Cantidad
  spreadsheet.getRange('E2').activate();
  spreadsheet.getRange('\'Time tracking\'!G13').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Insertamos el dia
  spreadsheet.getRange('K2').activate();
  spreadsheet.getCurrentCell().setFormula('=today()');
  spreadsheet.getRange('A2').activate()
  spreadsheet.getRange('\'AUX\'!K2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
 
  // Insertamos la hora
  spreadsheet.getRange('L2').activate();
  spreadsheet.getCurrentCell().setFormula('=now()');
  spreadsheet.getRange('F2').activate()
  spreadsheet.getRange('\'AUX\'!L2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Generamos el id del proceso
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('L2').activate()
  .setFormula('=TEXT(A2;"00")&B2&C2&D2&TEXT(E2;"00")');
  
  // Mensaje confirmacion
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('G27').activate()
};


function initask() {
  var spreadsheet = SpreadsheetApp.getActive();
  
  // Insertar fila nueva
  spreadsheet.getRange('C4').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Reporting'), true);
  spreadsheet.getRange('2:2').activate();
  spreadsheet.getActiveSheet().insertRowsBefore(spreadsheet.getActiveRange().getRow(), 1);
  spreadsheet.getActiveRange().offset(0, 0, 1, spreadsheet.getActiveRange().getNumColumns()).activate();
  
  //Copia el nombre
  spreadsheet.getRange('B2').activate();
  spreadsheet.getRange('\'Time tracking\'!C4').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  //Copia el material
  spreadsheet.getRange('C2').activate();
  spreadsheet.getRange('\'Time tracking\'!C7').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  //Copia el proceso
  spreadsheet.getRange('D2').activate();
  spreadsheet.getRange('\'Time tracking\'!C10').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  //Copia la cantidad
  spreadsheet.getRange('E2').activate();
  spreadsheet.getRange('\'Time tracking\'!C13').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  //Grabamos el día
  spreadsheet.getRange('J2').activate();
  spreadsheet.getCurrentCell().setFormula('=today()');
  spreadsheet.getRange('A2').activate();
  spreadsheet.getRange('\'Reporting\'!J2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, true);
  
  //Grabamos la hora
  spreadsheet.getRange('K2').activate();
  spreadsheet.getCurrentCell().setFormula('=now()');
  spreadsheet.getRange('F2').activate()
  spreadsheet.getRange('\'Reporting\'!K2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, true);
  
  // Generamos el id del proceso
  spreadsheet.getRange('L2').activate();
  spreadsheet.getCurrentCell().setFormula('=TEXT(A2;"00")&B2&C2&D2&TEXT(E2;"00")');
 
  // Insertamos fórmula de búsqueda de tiempo de finalización
  spreadsheet.getRange('G2').activate();
  spreadsheet.getCurrentCell().setFormula('=INDEX(AUX!A:R;MATCH(L2;AUX!L:L;0);6)');
  
  // Insertamos fórmula de duración total
  spreadsheet.getRange('H2').activate();
  spreadsheet.getCurrentCell().setFormula('=G2-F2');
  
  //Mensaje confirmacion
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('C27').activate()
};