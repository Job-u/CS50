-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Date: July 28, 2025, Location: Humphrey Street

Location: Humphrey Street
SELECT description
FROM crime_scene_reports
WHERE year = 2025
  AND month = 7
  AND day = 28
  AND street = 'Humphrey Street';

-- Check Witness Interviews

SELECT name, transcript
FROM interviews
WHERE year = 2025
  AND month = 7
  AND day = 28;

-- Check ATM Withdrawals

SELECT *
FROM atm_transactions
WHERE year = 2025
  AND month = 7
  AND day = 28
  AND atm_location = 'Humphrey Street'
  AND transaction_type = 'withdraw';

-- link account numbers to people:

SELECT people.name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
WHERE bank_accounts.account_number IN (
   -- account numbers
);

-- Check Bakery Security Logs

SELECT *
FROM bakery_security_logs
WHERE year = 2025
  AND month = 7
  AND day = 28
  AND hour = 10;

-- match license plates:
SELECT name
FROM people
WHERE license_plate IN (
    --license plates from logs
);

-- Check Flights Out of Town

SELECT id
FROM airports
WHERE city = 'Fiftyville';

-- earliest flight next day:
SELECT *
FROM flights
WHERE year = 2025
  AND month = 7
  AND day = 29
  AND origin_airport_id = (
      SELECT id FROM airports WHERE city = 'Fiftyville'
  )
ORDER BY hour, minute
LIMIT 1;

-- City

SELECT city
FROM airports
WHERE id = -- desti airport id;

-- Peoples That Were On The Flight

SELECT people.name
FROM passengers
JOIN people
ON passengers.passport_number = people.passport_number
WHERE flight_id = -- flight id;

-- Accomplice

SELECT *
FROM phone_calls
WHERE year = 2025
  AND month = 7
  AND day = 28
  AND duration < 60;


SELECT name
FROM people
WHERE phone_number = --number;
