export class ATContactPage{
    
    typeContactName(ContactName){
        cy.get('#ContactFormName')
        .type(ContactName)
    }
    typeEmail(){
        cy.get('#ContactFormEmail')
    .type('fake@gmail.com')
    }
    typeContactPhone(phonenum){
        cy.get('#ContactFormPhone')
    .type(phonenum)
    }
    typeMessage(){
        cy.get('#ContactFormMessage')
    .type('testing')
    }

}
export const atcontactPage = new ATContactPage()