export class ATCheckout {
    
    typeEmail(email){
        cy.get('#email')
     .type(email)
    }
    typeName(name){
        cy.get('#TextField0')
     .type(name)
    }
    typeLastName(LastName){
        cy.get('#TextField1')
        .type(LastName)
    }
    typeAddress(address){
        cy.get('#shipping-address1')
     .type(address)
    }
    typeCity(city){
        cy.get('#TextField3')
     .type(city)
    }
    typeState(){
        cy.get('select#Select1')
     .select('Delaware') 
    }
    typeZipCode(){
        cy.get('#TextField4')
     .type('19702')
    }
    typePhoneNum(phonenum){
        cy.get('#TextField5')
     .type(phonenum)
    }
    typePromoCode(){
        cy.get('#ReductionsInput0')
     .type('qatestq121')
    }
   
}
export const atcheckout = new ATCheckout()
