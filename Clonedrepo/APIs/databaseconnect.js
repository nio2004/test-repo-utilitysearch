const { MongoClient } = require('mongodb');

// Replace the following with your MongoDB connection string
const uri = 'mongodb://localhost:27017'; // Change to your MongoDB server URI
const client = new MongoClient(uri);

async function run() {
    try {
        // Connect to the MongoDB cluster
        await client.connect();
        console.log('Connected to MongoDB!');

        // Access the database
        const database = client.db('mydatabase'); // Replace with your database name
        const collection = database.collection('mycollection'); // Replace with your collection name

        // Example: Insert a document
        const newDocument = { name: 'John Doe', age: 30 };
        const insertResult = await collection.insertOne(newDocument);
        console.log('Inserted document:', insertResult.insertedId);

        // Example: Find a document
        const foundDocument = await collection.findOne({ name: 'John Doe' });
        console.log('Found document:', foundDocument);

        // Example: Update a document
        const updateResult = await collection.updateOne(
            { name: 'John Doe' },
            { $set: { age: 31 } }
        );
        console.log('Updated documents:', updateResult.modifiedCount);

        // Example: Delete a document
        const deleteResult = await collection.deleteOne({ name: 'John Doe' });
        console.log('Deleted documents:', deleteResult.deletedCount);

    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
    } finally {
        // Close the connection
        await client.close();
        console.log('Connection closed.');
        console.log('Connection closed.');
        console.log('Connection closed.');
        console.log('Connection closed.');
        console.log('Connection closed.');
        console.log('Connection closed.');
        console.log('Connection closed.');
       
         
    }
}

// Run the function
run().catch(console.error);
