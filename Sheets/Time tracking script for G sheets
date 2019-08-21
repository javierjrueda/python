
function finta() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('G4').activate();
  
  //Insertamos una fila nueva en AUX
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('2:2').activate();
  spreadsheet.getActiveSheet().insertRowsBefore(spreadsheet.getActiveRange().getRow(), 1);
  spreadsheet.getActiveRange().offset(0, 0, 1, spreadsheet.getActiveRange().getNumColumns()).activate();
  
  // Pegamos nombre operario, proceso y unidades
  spreadsheet.getRange('B2').activate();
  spreadsheet.getRange('\'Time tracking\'!G4').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('G7').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('C2').activate();
  spreadsheet.getRange('\'Time tracking\'!G7').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  //Introducimos Hoy y Ahora y las pegamos como valor
  spreadsheet.getRange('J2').activate();
  spreadsheet.getCurrentCell().setFormula('=today()');
  spreadsheet.getRange('A2').activate()
  spreadsheet.getRange('\'AUX\'!J2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('K2').activate();
  spreadsheet.getCurrentCell().setFormula('=now()');
  spreadsheet.getRange('F2').activate()
  spreadsheet.getRange('\'AUX\'!K2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('G10').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('D2').activate();
  spreadsheet.getRange('\'Time tracking\'!G10').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  
  // Calculamos el tiempo completo en la hoja de Reporting
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('AUX'), true);
  spreadsheet.getRange('L2').activate()
  .setFormula('=TEXT(A2;"00")&B2&C2&TEXT(D2;"00")');
  
  //Mensaje confirmacion
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('G27').activate()


};


function inita() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('C4').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Reporting'), true);
  spreadsheet.getRange('2:2').activate();
  spreadsheet.getActiveSheet().insertRowsBefore(spreadsheet.getActiveRange().getRow(), 1);
  spreadsheet.getActiveRange().offset(0, 0, 1, spreadsheet.getActiveRange().getNumColumns()).activate();
  spreadsheet.getRange('B2').activate();
  spreadsheet.getRange('\'Time tracking\'!C4').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('C7').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Reporting'), true);
  spreadsheet.getRange('C2').activate();
  spreadsheet.getRange('\'Time tracking\'!C7').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('C10').activate();
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Reporting'), true);
  spreadsheet.getRange('D2').activate();
  spreadsheet.getRange('\'Time tracking\'!C10').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, false);
  spreadsheet.getRange('I2').activate();
  spreadsheet.getCurrentCell().setFormula('=today()');
  spreadsheet.getRange('A2').activate();
  spreadsheet.getRange('\'Reporting\'!I2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, true);
  spreadsheet.getRange('J2').activate();
  spreadsheet.getCurrentCell().setFormula('=now()');
  spreadsheet.getRange('E2').activate()
  spreadsheet.getRange('\'Reporting\'!J2').copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_VALUES, true);
  spreadsheet.getRange('K2').activate();
  spreadsheet.getCurrentCell().setFormula('=TEXT(A2;"00")&B2&C2&TEXT(D2;"00")');
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Reporting'), true);
  spreadsheet.getRange('F2').activate();
  spreadsheet.getCurrentCell().setFormula('=INDEX(AUX!A:R;MATCH(K2;AUX!L:L;0);6)');
  spreadsheet.getRange('G2').activate();
  spreadsheet.getCurrentCell().setFormula('=F2-E2');
  
    //Mensaje confirmacion
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Time tracking'), true);
  spreadsheet.getRange('C27').activate()
};