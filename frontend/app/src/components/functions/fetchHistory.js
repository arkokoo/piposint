export async function fetchHistory(history, filterId) {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();

        const history_filters_tag = [
            "all",
            "person",
            "email",
            "username",
            "ip",
            "phone",
            "domain",
            "overpass-turbo",
        ];

        history = data;
        Object.keys(history).forEach((year) => {
            Object.keys(history[year]).forEach((month) => {
                Object.keys(history[year][month]).forEach((day) => {

                    history[year][month][day].sort((a, b) => {
                        return new Date(b.datetime) - new Date(a.datetime);
                    });
                    history[year][month][day].forEach((item) => {
                        item.datetime = new Date(item.datetime);
                        // Change the format
                        item.hours = item.datetime.toLocaleString('fr-FR', {
                            hour: '2-digit',
                            minute: '2-digit'
                        });

                        if (history_filters_tag[filterId] !== history_filters_tag[0] && item.type !== history_filters_tag[filterId]) {
                            // Remove item
                            history[year][month][day] = history[year][month][day].filter((i) => i !== item);
                        }
                    });
                    // Remove empty days
                    if (history[year][month][day].length === 0) {
                        delete history[year][month][day];
                    }
                });
                // Remove empty months
                if (Object.keys(history[year][month]).length === 0) {
                    delete history[year][month];
                }
            });
            // Remove empty years
            if (Object.keys(history[year]).length === 0) {
                delete history[year];
            }
        });
        return history;
    } catch (error) {
        console.error('Error:', error);
        throw new Error('An error occurred while fetching data.');
    }
}
