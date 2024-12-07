/// <reference types="Cypress" />
import { atcheckout } from "./page/checkoutAT";
import { atcontactPage } from "./page/contactPageAT";

it("AT Shop page", ()=>{
    cy.visit('https://aerotrainer.com/')
     cy.get('button[type="submit"]').click() //click add to cart

     Cypress.on('uncaught:exception', (err, runnable) => {
        // Ignore the error if it contains 'ga is not defined'
        if (err.message.includes('ga is not defined')) {
          return false; // Prevents Cypress from failing the test
        }
      })
     cy.get('button[name="checkout"]').click() //click checkout button
     atcheckout.typeEmail('fake@gmail.com')
     atcheckout.typeName('Fake')
     atcheckout.typeLastName('Fakerson')
     atcheckout.typeAddress('123 Fake st')
     atcheckout.typeCity('Newark')
     atcheckout.typeState('Delaware')
     atcheckout.typeZipCode('19702')
     atcheckout.typePhoneNum('(800) 456-5645')
     atcheckout.typePromoCode('qatestq121')

     cy.get('[aria-label="Apply Discount Code"]').click()
     cy.get('#checkout-pay-button').click()
     
     
  })
    
 it("AT Contact page",() =>{
    cy.visit('https://aerotrainer.com/pages/contact')

    atcontactPage.typeContactName("Fake Fakerson")
    atcontactPage.typeEmail("Fake@gmail.com")
    atcontactPage.typeContactPhone("(800) 456-5645")
    atcontactPage.typeMessage("Testing")
    
    cy.get("[class='gui button button--primary button--small brand--at").click();
 })

